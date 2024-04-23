from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo',views.create_todo,name="create_todo"),
    path('delete_todo',views.delete_todo,name="delete_todo"),
]
#새로 만든 urls파일
