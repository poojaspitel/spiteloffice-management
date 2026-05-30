#!/usr/bin/env bash
cd web
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate