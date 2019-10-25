#!/bin/bash

# It is responsability of the deployment orchestration to execute before
# migrations, create default admin user, populate minimal data, etc.

gunicorn binary_service.wsgi --config binary_service/gunicorn_conf.py
