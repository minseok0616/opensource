from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from todo_app.models import Todo
from django.urls import reverse

# Create your views here.

# url = ''
def index(request):
		_todos = Todo.objects.all()
		return render(request, 'index.html',{'todos': _todos})

def create_todo(request):
    content = request.POST['todoContent']
    new_todo = Todo(title=content)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def delete_todo(request):
    _id = request.GET['todoNum']
    todo = Todo.objects.get(id=_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))