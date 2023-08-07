from django.contrib import admin
from django.urls import path

{%- if cookiecutter.api != "No" %}
from {{cookiecutter.project_slug}}.core.api import api
{%- endif %}
from {{cookiecutter.project_slug}}.core.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    {%- if cookiecutter.api != "No" %}
    path("api/", api.urls),
    {%- endif %}
]
