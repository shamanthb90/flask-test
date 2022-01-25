#!/usr/bin/env bash

GUNICORN_PRELOAD_APP="${GUNICORN_PRELOAD_APP:-false}" \
GUNICORN_NUM_WORKERS="${GUNICORN_NUM_WORKERS:-1}" \
FLASK_CONFIG="${FLASK_CONFIG:-development}" \
exec gunicorn --config conf/gunicorn.conf.py wsgi:app
