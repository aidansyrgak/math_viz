from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("drawer/", views.drawer, name="drawer"),
    path("uploader/", views.uploader, name="uploader"),
    path("about/", views.about, name="about"),
    path("legal/", views.legal, name="legal"),
]