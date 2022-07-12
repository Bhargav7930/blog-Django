from django.contrib import admin
from django.urls import path
from home.view_api import LoginView, RegisterView
urlpatterns = [
    path('login/',LoginView,name='login' ),
    path('register/',RegisterView,name='register' ),
   
]