from django.urls import path
from . import views

#URLConf
#always end routes with forward slash /
urlpatterns = [
    path("hello/", views.say_hello)
]