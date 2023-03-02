from django.urls import path

from . import views


app_name = "my_quotes"

urlpatterns = [
    path("", views.index, name="index"),
]
