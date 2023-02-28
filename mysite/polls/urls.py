from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("mongo", views.connect_mongo, name="mongo")
]
