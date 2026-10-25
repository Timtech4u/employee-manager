FROM node:24-bookworm-slim AS frontend
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM python:3.11.16-slim-bookworm
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY --from=frontend /app/static-vuedj/ ./static-vuedj/
COPY --from=frontend /app/templates/index.html ./templates/index.html
RUN SECRET_KEY=build-only DATABASE_URL=postgresql://localhost/build python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["gunicorn", "vuedj.wsgi:application", "--bind", "0.0.0.0:8000", "--access-logfile", "-"]
