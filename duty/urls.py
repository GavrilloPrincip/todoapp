from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('create/',views.dutycreate, name = "dutycreate"),
    path('delete/<int:id>', views.dutydelete, name = 'dutydelete'),
    path('active/<int:id>', views.dutyactive, name = 'dutyactive'),

]
