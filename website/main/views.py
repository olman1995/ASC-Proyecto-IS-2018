from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import usuario

def index(request):
    template = loader.get_template('main.html')
    print(usuario.objects.all())
    context={}
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login.html')
    
    context={}
    return HttpResponse(template.render(context,request))