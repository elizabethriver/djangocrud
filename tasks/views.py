from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def listTasks(request):
    tasks = Task.objects.all()
    return render(request, 'list.html', {"tasks": tasks} )

def createTaks(request):
    task = Task(title = request.POST['title'], description = request.POST['description'])
    task.save()
    return redirect('/tasks/')

def removeTasks(request, id):
    instance = Task.objects.get(id=id)
    instance.delete()
    return redirect('/tasks/')