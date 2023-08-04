from django.contrib import admin
from django.urls import path

from {{cookiecutter.project_slug}}.core.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
]
