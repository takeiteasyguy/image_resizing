import os

import gevent.socket
import redis.connection
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer


redis.connection.socket = gevent.socket
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = uWSGIWebsocketServer()
