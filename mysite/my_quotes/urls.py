from django.urls import path

from . import views


app_name = "my_quotes"

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<author_name>", views.get_author, name="author"),
    path("<tag>", views.get_quotes_by_tags, name="tag")
]
