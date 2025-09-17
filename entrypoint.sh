python manage.py migrate

python manage.py collectstatic --noinput

gunicorn core.wsgi:application -w 5 --bind 0.0.0.0:8000