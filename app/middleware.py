from __future__ import absolute_import, division, print_function
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session


try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()

def get_current_request():
    """ returns the request object for this thread """
    return getattr(_thread_locals, "request", None)

def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)

class ThreadLocalMiddleware(MiddlewareMixin):
    """ Simple middleware that adds the request object in thread local stor    age."""

    def process_request(self, request):
        _thread_locals.request = request

    def process_response(self, request, response):
        if hasattr(_thread_locals, 'request'):
            del _thread_locals.request
            return response