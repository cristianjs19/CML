TO RUN PROJECT:
###############

1) Create and activate a virtual environment.
2) ``pip install -r requirements.txt``
3) ``python manage.py makemigrations`` *app
4) ``python manage.py migrate``
5) ``python manage.py createsuperuser`` 
6) ``python manage.py runserver``

## Others
- python3 manage.py showmigrations
- python3 manage.py sqlmigrate bookingApp 0001_initial // Cretae tables


TO RUN TESTS:
-------------
``python manage.py test``

``python manage.py test <app>`` 



CURL

Qualifier
`curl -X POST  -H "Content-Type: application/json" http://127.0.0.1:8000/qualifier/   -d '{"author": "lal", "title": "lala", "description": "lalal", "genre": "action", "status": "available", "cover": null, "user":"1"}'`
