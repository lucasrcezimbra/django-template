from django.contrib import admin
from django.urls import path

{% if cookiecutter.api != "No" -%}
from {{cookiecutter.project_slug}}.core.api import api
{% endif -%}
{% if cookiecutter.html != "No" -%}
from {{cookiecutter.project_slug}}.core.views import index
{%- endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
    {%- if cookiecutter.html != "No" %}
    path("", index, name="index"),
    {%- endif %}
    {%- if cookiecutter.api != "No" %}
    path("api/", api.urls),
    {%- endif %}
]
