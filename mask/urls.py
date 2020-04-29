from django.contrib import admin
from django.urls import path
from . import views

app_name="mask"
urlpatterns = [
    path('', views.homepage,name="homepage"),
]