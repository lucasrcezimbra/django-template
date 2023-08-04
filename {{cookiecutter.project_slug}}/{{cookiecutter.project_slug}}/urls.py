from django.contrib import admin
from django.urls import path

{%- if cookiecutter.use_django_ninja == 'True' %}
from {{cookiecutter.project_slug}}.core.api import api
{%- endif %}
from {{cookiecutter.project_slug}}.core.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    {%- if cookiecutter.use_django_ninja == 'True' %}
    path("api/", api.urls),
    {%- endif %}
]
