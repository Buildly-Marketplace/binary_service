#!/bin/bash

python manage.py migrate

gunicorn binary_service.wsgi --config binary_service/gunicorn_conf.py
