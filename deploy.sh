#!/usr/bin/env sh
set -eu
python -m pip install -r requirements.txt
npm ci
npm run build
python manage.py collectstatic --noinput
python manage.py migrate_schemas --noinput
exec gunicorn vuedj.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --access-logfile -
