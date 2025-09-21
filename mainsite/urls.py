from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("solutions", views.solutions, name="solutions"),
    path("userPage", views.userPage, name="userPage"),
    path("regLog", views.regLogPage, name="regLog")
]
