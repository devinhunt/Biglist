from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from hailpixel.biglist.models import Todo
from hailpixel.biglist.forms import AddTaskForm

def index(request):
    active_todos = Todo.objects.filter(active = True)
    return render_to_response('index.html', {
        'todos' : active_todos.filter(done = False).order_by('-created'),
        'dones' : active_todos.filter(done = True).order_by('-finished')
    })

@login_required
def inbox(request):
    return render_to_response('inbox.html', {
        'todos' : Todo.objects.filter(active = False).filter(done = False)
    })
    
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        
        if form.is_valid():
            if request.user.is_authenticated():
                # The owner is generating this task, so it's automatically added to the main list
                task = Todo(task = form.cleaned_data['task'], active = True)
                task.save()
            
                # And generate the html response
                task_html = render_to_string('task.html', {'todo' : task})
                data = '{"active" : true}'
            else:
                task = Todo(task = form.cleaned_data['task'], active = False)
                task.save()
            
                # And generate the html response
                task_html = render_to_string('task_pending.html', {'todo' : task})
                data = '{"active" : false}'
            
            return HttpResponse(ajax_response(html_data = task_html, data = data))
        else:
            return HttpResponse(ajax_response(False))
    else:
        form = AddTaskForm()
    
    return render_to_response('add.html', {
        'form' : form
    })

@login_required
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

@login_required
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

@login_required
def modify_task(request):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(pk = request.POST.get('todo_pk'))
            action = request.POST.get('action')
            if action == 'accept':
                todo.active = True
                todo.save()
            else:
                todo.delete()
            return HttpResponse(ajax_response(True));
        except:
            return HttpResponse(ajax_response(False));
    else:
        return HttpResponse(ajax_response(False));
    
def ajax_response(success = True, html_data = '', data = '{}'):
    if success:
        return '{"success" : true , "html" : "%s", "data" : %s}' % (html_data.replace('"', '\\"').replace('\n', '\\n'), data)
    else:
        return '{"success" : false , "html" : "%s", "data" : %s}' % (html_data.replace('"', '\\"').replace('\n', '\\n'), data)