from django.urls import path
from .views import Hello_world, add, create_user, get_user

urlpatterns = [
    path("hello", Hello_world, name = "Hello"),
    path("Add", add, name = "add"),
    path("AddUser", create_user, name = "new_user"),
    path("GetUser", get_user, name= "display_user")
]

