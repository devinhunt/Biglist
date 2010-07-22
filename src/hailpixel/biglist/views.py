from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import render_to_string
from hailpixel.biglist.models import Todo
from hailpixel.biglist.forms import AddTaskForm

def index(request):
    return render_to_response('index.html', {
        'todos' : Todo.objects.all().filter(done = False).order_by('-created'),
        'dones' : Todo.objects.all().filter(done = True).order_by('-finished')
    })
    
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        
        if form.is_valid():
            
            # Save the task
            task = Todo(task = form.cleaned_data['task'])
            task.save()
            
            # And generate the html response
            task_html = render_to_string('task.html', {'todo' : task})
            
            return HttpResponse(ajax_response(html_data = task_html))
        else:
            return HttpResponse(ajax_response(False, task_html))
    else:
        form = AddTaskForm()
    
    return render_to_response('add.html', {
        'form' : form
    })
    
def mark_todo_complete(request):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(pk = request.POST.get('todo_pk'))
            todo.done = True
            todo.finished = datetime.now()
            todo.save()
            task_html = render_to_string('task.html', {'todo' : todo})
            
            return HttpResponse(ajax_response(True, task_html));
        except:
            return HttpResponse(ajax_response(False));
        
    else:
        return HttpResponse(ajax_response(False));
        
def mark_todo_incomplete(request):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(pk = request.POST.get('todo_pk'))
            todo.done = False
            todo.created = datetime.now()
            todo.save()
            task_html = render_to_string('task.html', {'todo' : todo})
            
            return HttpResponse(ajax_response(True, task_html));
        except:
            return HttpResponse(ajax_response(False));
    else:
        return HttpResponse(ajax_response(False));
    
def ajax_response(success = True, html_data = '', data = ''):
    if success:
        return '{"success" : true , "html" : "%s", "data" : "%s"}' % (html_data.replace('"', '\\"').replace('\n', '\\n'), data)
    else:
        return '{"success" : false , "html" : "%s"}' % (html_data.replace('"', '\\"').replace('\n', '\\n'), data)