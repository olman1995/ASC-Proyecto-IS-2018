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
    if request.method == 'POST':
        context={}
        #return HttpResponseRedirect("/inicio")
        nombre = request.POST['nombre']
        contrasena = request.POST['contrasena']
        
        for i in usuario.objects.all():
            if i.nombre==nombre and i.contrasena == contrasena:
                template = loader.get_template('main.html')
                return HttpResponse(template.render(context,request))
                
        return HttpResponse(template.render(context,request))
    else:
        context={}
        return HttpResponse(template.render(context,request))