"""
WSGI config for image resizing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import gevent.socket
import redis.connection
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

if 'WEB_SOCKET' in os.environ:
    # run websocket application
    redis.connection.socket = gevent.socket
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    application = uWSGIWebsocketServer()
else:
    # run common wsgi application
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    application = get_wsgi_application()
