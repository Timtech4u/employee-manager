# Python 3.11 dependency upgrade

Scope: upgrade runtime and all dependencies while preserving PostgreSQL tenant schemas, existing models and routes.

Implementation sequence: resolve Python 3.11-compatible releases; exercise startup and tenant/API/image behavior on an isolated PostgreSQL database; replace removed Django URL, storage, schema documentation and test-runner APIs; upgrade Vue/build dependencies separately; verify fresh installation, migrations, tests, static collection and dependency audits; prepare a pull request.

Django 5.2 LTS is the newest Django series supporting Python 3.11. Keep django-tenant-schemas to preserve the existing domain/schema model. Remove unused legacy auth/JWT packages rather than introducing new authentication endpoints. Replace CoreAPI documentation with OpenAPI documentation at the existing /docs/ route. Keep AutoField IDs to avoid unintended primary-key migrations.

Review focus: existing tenant schema compatibility, tenant isolation, login/profile signals, image validation, frontend static paths, and security advisory resolution. Production data migration and deployment require separate verification against a backup of the real database.
