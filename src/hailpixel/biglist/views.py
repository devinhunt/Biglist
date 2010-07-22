from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from hailpixel.biglist.models import Todo
from hailpixel.biglist.forms import AddTaskForm

def index(request):
    return render_to_response('index.html', {'todos' : Todo.objects.all()})
    
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        
        if form.is_valid():
            task = Todo(task = form.cleaned_data['task'])
            task.save()
            return HttpResponse('{"success" : "true" , "task_html" : "<div>NEW TASK</div>"}')
        else:
            return HttpResponse('{"success" : "false" }')
    else:
        form = AddTaskForm()
    
    return render_to_response('add.html', {
        'form' : form
    })