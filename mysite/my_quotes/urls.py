from django.urls import path

from . import views


app_name = "my_quotes"

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<int:numb_page>", views.index, name="next_page"),
    path("author/<author_name>", views.get_author, name="author"),
    path("tag/<tag>", views.tag, name="tag"),
    # path("login/", views.login, name="login"),
    # path("register/", views.register, name="register"),
]
