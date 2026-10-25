from datetime import date
from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import connection
from customers.models import Client
from PIL import Image
from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient

from app.models import Organization, Profile
from app.serializers import ProfileSerializer


class ApplicationTests(TenantTestCase):
    @classmethod
    def setUpClass(cls):
        cls.sync_shared()
        cls.add_allowed_test_domain()
        cls.tenant = Client(domain_url='tenant.test.com', schema_name='test',
                            name='Test employer', paid_until=date(2099, 12, 31),
                            on_trial=False)
        cls.tenant.save(verbosity=0)
        cls.other_tenant = Client(domain_url='other.test.com', schema_name='other_test',
                                  name='Other employer', paid_until=date(2099, 12, 31),
                                  on_trial=False)
        cls.other_tenant.save(verbosity=0)
        connection.set_tenant(cls.tenant)

    @classmethod
    def tearDownClass(cls):
        connection.set_schema_to_public()
        cls.other_tenant.delete(force_drop=True)
        super().tearDownClass()

    def setUp(self):
        connection.set_tenant(self.tenant)
        self.client = TenantClient(self.tenant)

    def test_jobs_page_and_admin_login(self):
        self.assertContains(self.client.get('/jobs/'), 'id="app"')
        self.assertContains(self.client.get('/login/'), 'csrfmiddlewaretoken')

    def test_user_creation_and_login_preserve_profile(self):
        user = User.objects.create_user('employee', password='test-password-123')
        self.assertEqual(Profile.objects.get(user=user).user_id, user.pk)
        self.assertTrue(self.client.login(username='employee', password='test-password-123'))
        user.refresh_from_db()
        self.assertEqual(Profile.objects.filter(user=user).count(), 1)

    def test_organization_api(self):
        Organization.objects.create(name='Test employer', email='test@example.com')
        response = self.client.get('/api/organization/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['name'], 'Test employer')

    def test_image_upload_validation(self):
        image = BytesIO()
        Image.new('RGB', (8, 8), 'blue').save(image, 'PNG')
        field = ProfileSerializer().fields['passport']
        upload = SimpleUploadedFile('portrait.png', image.getvalue(), content_type='image/png')
        self.assertEqual(field.run_validation(upload).name, 'portrait.png')
        from django.core.exceptions import ValidationError
        with self.assertRaises(ValidationError):
            field.run_validation(SimpleUploadedFile('bad.png', b'not an image'))

    def test_api_documentation_and_schema(self):
        self.assertEqual(self.client.get('/docs/').status_code, 200)
        response = self.client.get('/api/schema/', HTTP_ACCEPT='application/vnd.oai.openapi+json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('/api/organization/', response.json()['paths'])
        schemas = response.json()['components']['schemas']
        self.assertIn('name', schemas['app_department_depth0']['properties'])
        self.assertIn('username', schemas['auth_user_depth0']['properties'])

    def test_tenant_data_and_upload_paths_are_isolated(self):
        from django.core.files.storage import default_storage
        connection.set_tenant(self.tenant)
        Organization.objects.create(name='First employer', email='first@example.com')
        first_path = default_storage.path('passports/avatar.png')
        other_client = TenantClient(self.other_tenant)
        self.assertEqual(other_client.get('/api/organization/').json(), [])
        other_path = default_storage.path('passports/avatar.png')
        self.assertNotEqual(first_path, other_path)
        self.assertEqual(self.client.get('/api/organization/').json()[0]['name'], 'First employer')

    def test_unknown_tenant_returns_404(self):
        self.assertEqual(self.client.get('/api/organization/', HTTP_HOST='unknown.test.com').status_code, 404)

    def test_admin_login_with_csrf(self):
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'test-admin-password')
        connection.set_tenant(self.other_tenant)
        User.objects.create_superuser('other_admin', 'other@example.com',
                                      'different-password', id=admin.pk)
        connection.set_tenant(self.tenant)
        client = TenantClient(self.tenant, enforce_csrf_checks=True)
        self.assertEqual(client.get('/login/').status_code, 200)
        response = client.post('/login/', {
            'username': 'admin', 'password': 'test-admin-password', 'next': '/',
            'csrfmiddlewaretoken': client.cookies['csrftoken'].value,
        })
        self.assertEqual(response.status_code, 302)
        self.assertContains(client.get('/'), 'Site administration')
        # Shared session cookies must not authenticate a user in another tenant.
        other = TenantClient(self.other_tenant)
        other.cookies = client.cookies
        response = other.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_production_frontend_assets_are_served(self):
        import re
        from django.test import override_settings
        with override_settings(DEBUG=False):
            client = TenantClient(self.tenant)
            page = client.get('/jobs/')
            self.assertEqual(page.status_code, 200)
            assets = re.findall(r'(?:src|href)="(/staticfiles/assets/[^"]+)"', page.content.decode())
            self.assertTrue(any(path.endswith('.js') for path in assets))
            self.assertTrue(any(path.endswith('.css') for path in assets))
            for path in assets:
                response = client.get(path)
                self.assertEqual(response.status_code, 200, path)
                self.assertGreater(len(b''.join(response.streaming_content)), 0)
