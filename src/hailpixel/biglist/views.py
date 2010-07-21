from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from hailpixel.biglist.models import Todo

def index(request):
    return render_to_response('index.html', {'todos' : Todo.objects.all()})