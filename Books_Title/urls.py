from django.contrib import admin
from django.urls import path, include
from Books_Title import views

urlpatterns = [
    path('', views.BookSearch, name="BookSearch"),
]