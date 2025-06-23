#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn notes_project.wsgi --bind 0.0.0.0:$PORT
