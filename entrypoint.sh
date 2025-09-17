python manage.py migrate

python manage.py collectstatic --noinput

gunicorn ecommerce_vr.wsgi:application -w 5 --bind 0.0.0.0:8000