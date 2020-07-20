from django.contrib import admin
from django.urls import path
from .views import index, taskTwo
urlpatterns = [
    path('', index, name='home'),
    path('<int:start>-<int:end>', taskTwo, name='home'),
]
