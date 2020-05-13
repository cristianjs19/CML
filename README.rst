TO RUN PROJECT:
###############

1) Create and activate a virtual environment.
2) ``pip install -r requirements.txt``
3) ``python manage.py makemigrations``
4) ``python manage.py migrate``
5) ``python manage.py createsuperuser``
6) ``python manage.py runserver``


## Database migrations

- python3 manage.py makemigrations
- python3 manage.py showmigrations
- python3 manage.py sqlmigrate bookingApp 0001_initial // Cretae tables
- python3 manage.py migrate


CURL

curl -X POST  -H "Content-Type: application/json" http://127.0.0.1:8000/booking/list  -d '{"author": "lal", "title": "lala", "description": "lalal", "genre": "action", "status": "available", "cover": null, "user":"1"}'