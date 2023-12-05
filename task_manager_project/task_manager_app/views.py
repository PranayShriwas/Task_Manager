# task_manager/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django import forms

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        status = request.POST['status']

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status,
            user=request.user
        )

        return redirect('task_list')

    return render(request, 'create_task.html')
