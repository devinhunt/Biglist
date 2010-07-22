from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import render_to_string
from hailpixel.biglist.models import Todo
from hailpixel.biglist.forms import AddTaskForm

def index(request):
    return render_to_response('index.html', {'todos' : Todo.objects.all().order_by('-created')})
    
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        
        if form.is_valid():
            
            # Save the task
            task = Todo(task = form.cleaned_data['task'])
            task.save()
            
            # And generate the html response
            task_html = render_to_string('task.html', {'todo' : task}).replace('"', '\\"').replace('\n', '\\n')
            print task_html
            
            return HttpResponse('{"success" : true , "task_html" : "%s"}' % (task_html))
        else:
            return HttpResponse('{"success" : false }')
    else:
        form = AddTaskForm()
    
    return render_to_response('add.html', {
        'form' : form
    })