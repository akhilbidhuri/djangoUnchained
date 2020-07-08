release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py populate data.json

web: gunicorn djangoUnchained.wsgi