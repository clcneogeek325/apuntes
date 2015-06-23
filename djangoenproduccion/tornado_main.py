#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import sys
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
sys.path.append("/home/flor/entornos/django1.7/lib/python2.7/site-packages")
#sys.path.append("/home/flor/proyectos/demo/")
sys.path.append("/home/flor/entornos/django1.7/lib/python2.7/site-packages/django/contrib/admin/static")


def main():
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings' # path to your settings module
    application = django.core.handlers.wsgi.WSGIHandler()
    application = get_wsgi_application()
    container = tornado.wsgi.WSGIContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(9000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":


