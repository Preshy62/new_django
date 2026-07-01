from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name="home"),      # Home page
    path("about/", views.about, name="about"),
    path("student/", views.student, name="student"),
]