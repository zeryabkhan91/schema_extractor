import json
import threading
from django.urls import resolve
from sqlalchemy import create_engine

_thread_locals = threading.local()

class DatabaseCredentialsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
      if request.method == "POST" and resolve(request.path_info).url_name == "credentials":
          data = json.loads(request.body.decode('utf-8'))
          host = data.get('host')
          username = data.get('username')
          password = data.get('password')
          database = data.get('database')

          if all([host, username, password, database]):
              credentials = {
                  "NAME": database,
                  "USER": username,
                  "PASSWORD": password,
                  "HOST": host,
                  'PORT': '5432',
              }
              
              engine = create_engine(
              f"postgresql://{credentials['USER']}:{credentials['PASSWORD']}@{credentials['HOST']}:{credentials['PORT']}/{credentials['NAME']}"
              )

              _thread_locals.credentials = credentials
              _thread_locals.engine = engine
          else:
              _thread_locals.credentials = None
              _thread_locals.engine = None

      return None

    def __call__(self, request):
        response = self.get_response(request)
        return response
