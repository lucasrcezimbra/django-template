from django.contrib import admin
from django.urls import path

from test_project.core.api import api
from test_project.core.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("api/", api.urls),
]
