from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.db import models

import os

from main.models import usuario
from main.back_end.control.UIUsuario import UIUsuario

usuario = UIUsuario()

def index(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def medico(request):
    template = loader.get_template('medico.html')
    context={}
    return HttpResponse(template.render(context,request))

def cargar_imagen(request):
    template = loader.get_template('cargar_imagen.html')
    
    if request.method == 'POST':
        print("imagen 1")
        subir_imagen(request.FILES['img'])
        context={}
        return HttpResponse(template.render(context,request))
    context={}
    return HttpResponse(template.render(context,request))


def subir_imagen(file):
    directory=os.path.split(os.path.abspath(__file__))[0]+'/media/upload/'
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    fs = FileSystemStorage(location=directory)
    filename = fs.save(str(file), file)
    uploaded_file_url = fs.url(filename)

    return True

def cargar_paciente(request):
    template = loader.get_template('cargar_paciente.html')
    context={}    
    return HttpResponse(template.render(context,request))

def principal(request):
    template = loader.get_template('principal.html')
    context={}    
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login_datos.html')
    if request.method == 'POST':
        context={}
        #return HttpResponseRedirect("/inicio")
        nombre = request.POST['nombre']
        contrasena = request.POST['contrasena']
        usuario.ingresar(nombre,contrasena)
        return HttpResponseRedirect("principal")            
        #return HttpResponse(template.render(context,request))
    else:
        context={}
        return HttpResponse(template.render(context,request))