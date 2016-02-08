from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt 

from .models import TodoList

# Create your views here.

class TodoListView(ListView):
    
    model = TodoList
    template_name = "todo_list.html"
    context_object_name = "todo_list"

@csrf_exempt
def Todo(request):
    context = {}
    if request.method=="POST":
        name = request.POST.get('name', None)
        
        new_task, created = TodoList.objects.get_or_create(name=name)
        new_task.status = False
        
        
        new_task.save()
        
    
    
    return render_to_response('todo_form.html', context)