from django.urls import path
from .views import task_list, create_task
urlpatterns = [
    
    path('task-list/', task_list, name='task_list'),
    path('create-task/', create_task, name='create_task'),
]
