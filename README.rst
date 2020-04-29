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