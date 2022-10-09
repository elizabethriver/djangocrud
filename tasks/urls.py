from django.urls import path

from . import views

urlpatterns = [
    path('', views.listTasks),
    path('new/', views.createTaks, name='create_task'),
    path('delete/<int:id>', views.removeTasks, name='delete'),

]