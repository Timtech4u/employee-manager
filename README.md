# Employee Manager

A Django 5.2 LTS / Vue 3 application with PostgreSQL schema-based tenancy.

## Requirements

- Python 3.11 (pinned to 3.11.16)
- Node.js 24 LTS (24.15 or newer) and npm
- PostgreSQL 16

## Development

```sh
python3.11 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
npm ci
npm run build
export SECRET_KEY='your-local-development-key'
export DATABASE_URL='postgresql://user:password@localhost/employee_manager'
python manage.py migrate_schemas --shared
python manage.py collectstatic --noinput
python manage.py shell
```

Create the public tenant and a tenant in the shell (domains must match the HTTP host):

```python
from customers.models import Client
Client(domain_url='127.0.0.1', schema_name='public', name='Public',
       paid_until='2099-12-31', on_trial=False).save()
Client(domain_url='localhost', schema_name='client', name='Employer',
       paid_until='2099-12-31', on_trial=False).save()
```

Run `python manage.py runserver`, then open `http://localhost:8000/jobs/`.
Use `python manage.py tenant_command createsuperuser --schema=client` to create a tenant administrator. The existing profile signal requires a tenant schema containing the `app` tables; create employee users within tenant schemas.

For frontend hot reload, run `npm run dev` alongside Django. The development proxy defaults to `http://localhost:8000`; override with `DJANGO_DEV_ORIGIN` if necessary. Use a host registered to a tenant.

## Routes

- `/`: Django administration
- `/jobs/`: organization and tenant directory
- `/api/`: existing REST endpoints
- `/docs/`: OpenAPI UI (Swagger assets load from its configured CDN)
- `/api/schema/`: OpenAPI schema

## Verification

Use a dedicated PostgreSQL database and a user allowed to create test databases and schemas:

```sh
npm run lint
npm test
npm run build
python manage.py collectstatic --noinput
python manage.py makemigrations --check --dry-run
coverage run --source=app,customers manage.py test --noinput
pip check
pip-audit -r requirements.txt --no-deps --disable-pip
npm audit
```

Tests create and remove a separate test database. They exercise tenant isolation, upload paths, login/profile creation, image validation, API documentation and page routes. GitHub Actions runs the same checks with PostgreSQL 16, Python 3.11 and Node 24.

## Deployment and upgrading

The Dockerfile uses a Node build stage and a Python 3.11 runtime, serving with Gunicorn and WhiteNoise. Supply `SECRET_KEY` and `DATABASE_URL` at runtime; persist `media/` separately. `deploy.sh` installs locked dependencies, builds assets, collects static files and migrates public and tenant schemas before starting Gunicorn. Run it only as an intentional release operation.

This upgrade preserves the existing models and migration history. Before upgrading an existing deployment, back up the database and uploads, rehearse `migrate_schemas --noinput` on a restored copy, and verify tenant login and uploads. This repository update does not migrate or deploy production data. Existing broad API access and public tenant listing are unchanged; review those application permissions before exposing a new deployment.

Pillow 13.0.0 resolves CVE-2026-112895. Django stays on the latest 5.2 LTS patch because newer Django series require newer Python. Retired, unused django-rest-auth/JWT packages and nose/coveralls are removed; Django's test runner and coverage replace nose. OpenAPI replaces retired CoreAPI documentation. Vue 3 and Vite replace Vue 2/Webpack 3; unused UI packages are removed.

Dependency inputs are `requirements.in` and `requirements-dev.in`. Refresh locks with uv:

```sh
uv pip compile --upgrade --python 3.11 requirements.in -o requirements.txt
uv pip compile --upgrade --python 3.11 requirements-dev.in -c requirements.txt -o requirements-dev.txt
```

The original project accompanied a PyConNG talk on Django multitenancy.
