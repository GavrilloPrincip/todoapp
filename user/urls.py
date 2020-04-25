from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registerpage, name = "registerpage"),
    path('login/', views.loginpage, name = 'loginpage'),
    path('logout/', views.logoutpage, name='logoutpage'),
]
