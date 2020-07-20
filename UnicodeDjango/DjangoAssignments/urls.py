from django.contrib import admin
from django.urls import path
from .views import index, taskTwo, taskThree, taskFourA, taskFourB
urlpatterns = [
    path('', index, name='home'),
    path('taskTwo/<int:start>-<int:end>', taskTwo, name='taskTwo'),
    path('taskThree', taskThree, name='taskThree'),
    path('taskFourA', taskFourA, name='taskFourA'),
    path('taskFourB', taskFourB, name='taskFourB'),
]
