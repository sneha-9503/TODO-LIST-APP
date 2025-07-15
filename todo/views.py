from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request,'todo/index.html' , {'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        Todo.objects.create(task=task, description=description)
    return redirect('todo_list')

def complete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_todo(request,todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')



def update_todo(request, todo_id):
    todo = Todo.objects.get( id=todo_id)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the todo list or another page
    else:
        form = TodoForm(instance=todo)
    
    return render(request, 'todo/update_todo.html', {'form': form, 'todo': todo})