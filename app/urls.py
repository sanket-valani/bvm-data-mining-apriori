from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", views.default),
    url(r"^result/$", views.result),
]
