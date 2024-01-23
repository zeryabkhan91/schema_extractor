from django.urls import re_path
from .views import credentials, schema, search_table

urlpatterns = [
    re_path(r'^credentials/?$', credentials, name='credentials'),
    re_path(r'^schema/?$', schema, name='schema'),
    re_path(r'^search/(?P<table_name>[\w-]+)/?$', search_table, name='search_table'),
]