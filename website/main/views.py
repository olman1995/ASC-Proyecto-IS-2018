from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.db import models
from numpy import genfromtxt
import pandas as pd

import os
import shutil

from main.models import usuario
from main.back_end.control.UIUsuario import UIUsuario
from main.back_end.control.DaoBDPaciente import DaoBDPaciente
from main.back_end.control.DTOPaciente import DTOPaciente

usuario = UIUsuario()

def index(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context,request))

def medico(request):
    template = loader.get_template('medico.html')
    context={}
    return HttpResponse(template.render(context,request))

def subir_muestra(file):
    directory=os.path.split(os.path.abspath(__file__))[0]+'/media/test/'
    shutil.rmtree(directory)
    
    if not os.path.exists(directory):
            os.makedirs(directory)
            
    for afile in file.FILES.getlist('file'):
        
        fs = FileSystemStorage(location=directory)
        filename = fs.save(str(afile), afile)
        uploaded_file_url = fs.url(filename)

def subir_csv(file):
    directory_1=os.path.split(os.path.abspath(__file__))[0]+'/media/csv/'
    fs_1 = FileSystemStorage(location=directory_1)
    filename_2 = fs_1.save(str(file), file)
    return filename_2     
    

def resultado(request):
    template = loader.get_template('resultado.html')
    context={}
    return HttpResponse(template.render(context,request))


def cargar_muestra(request):
    template = loader.get_template('cargar_muestra.html')
    context={}
    if request.method == 'POST':
        template = loader.get_template('resultado.html')
        subir_muestra(request)
        subir_csv(request.FILES['csv'])
        
        directory=os.path.split(os.path.abspath(__file__))[0]+'/media/test/'
        nombres_archivos = os.listdir(directory)
        
        directory_1=os.path.split(os.path.abspath(__file__))[0]+'/media/csv/'+str(request.FILES['csv'])
        #
        leer=pd.read_csv(directory_1,sep=',');
        #print(leer.values())
        muestra={"id":[],"age":[],"sex":[]}
        for i in range(len(leer.get("id"))):
            #print(leer.get("id")[i])
            for nombre_archivo in nombres_archivos:
                #print(nombre_archivo.split()[0])
                if str(leer.get("id")[i]) == nombre_archivo.split(".")[0]:
                    muestra.get("id").append(leer.get("id")[i])
                    muestra.get("age").append(leer.get("boneage")[i])
                    if(leer.get("male")[i]==True):
                        muestra.get("sex").append("M")
                    else:
                        muestra.get("sex").append("F")
        
        
        k=int(request.POST["k"])
        cant_img=int(request.POST["cant_img"])
        resultado = usuario.facade.cargar_muestra(muestra,k,cant_img)
        res = []
        for i in range(k):
            res.append({"sub":[],
                        "mae":resultado.get('mae')[i],
                        "mse":resultado.get('mse')[i],
                        "res":resultado.get('res')[i],
                        "mean":resultado.get('mean')[i],
                        "std":resultado.get('std')[i],
                        "var":resultado.get('var')[i]})
            for k in range(cant_img):
                
                info={"id":resultado.get('sub')[i][0][k],
                      "edad":resultado.get('sub')[i][1][k], 
                      "sexo":resultado.get('sub')[i][2][k] ,
                      "estimacion":resultado.get('res')[i][k]}
                
                res[i].get("sub").append(info)
        
        context={"res":res}
        
        
    #context={}
    return HttpResponse(template.render(context,request))

def cargar_imagen(request):
    template = loader.get_template('cargar_imagen.html')
    
    if request.method == 'POST':
        
        template = loader.get_template('cargar_paciente.html')
        img_name=subir_imagen(request.FILES['img'])
        usuario.facade.estimar_edad(request.POST["sexo"],img_name)
        edad,estimacion=usuario.facade.desplegar_edad()
        context={"estimacion":estimacion,"img":img_name}
        return HttpResponse(template.render(context,request))
    context={}
    return HttpResponse(template.render(context,request))


def subir_imagen(file):
    directory_1=os.path.split(os.path.abspath(__file__))[0]+'/static/media/upload/'
    directory_2=os.path.split(os.path.abspath(__file__))[0]+'/back_end/modelo/BoneAge_XRay_CNN/dataset/test/'
    shutil.rmtree(directory_2)
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    fs_1 = FileSystemStorage(location=directory_1)
    fs_2 = FileSystemStorage(location=directory_2)
    filename_2 = fs_1.save(str(file), file)
    filename_1 = fs_2.save(str(file), file)
    return filename_2 
    #uploaded_file_url = fs_1.url(filename_1)
    #uploaded_file_url = fs_2.url(filename_2)


    return True

def cargar_paciente(request):
    template = loader.get_template('cargar_paciente.html')
    context={}    
    if request.method == 'POST':
        template = loader.get_template('cargar_paciente.html')
        edad=int(request.POST["edad"])
        estimacion_edad=0
        url_imagen="media/upload/"+request.POST["url"]
        nombre=request.POST["nombre"]
        apellido_1=request.POST["apellido1"]
        apellido_2=request.POST["apellido2"]
        cedula=request.POST["cedula"]
        hospital=request.POST["hospital"]
        datos= DTOPaciente(edad,estimacion_edad,url_imagen,nombre,apellido_1,apellido_2,cedula,hospital)
        usuario.facade.guardar_informacion_paciente(datos)
        return HttpResponse(template.render(context,request))
    return HttpResponse(template.render(context,request))

def ver_pacientes(request):
    template = loader.get_template('ver_pacientes.html')
    res=usuario.facade.cargar_informacion()
    context={"res":res}    
    return HttpResponse(template.render(context,request))

def principal(request):
    template = loader.get_template('principal.html')
    context={}    
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login_datos.html')
    if request.method == 'POST':
        
        
        
        nombre = request.POST['nombre']
        contrasena = request.POST['contrasena']
        tipo = usuario.ingresar(nombre,contrasena)
        
        if tipo==0:
            
            template = loader.get_template('cargar_muestra.html')
            modo_1 = "display:none"
            modo_2 = ""
            context={"modo_1":modo_1,"modo_2":modo_2}
            return HttpResponse(template.render(context,request))
        elif tipo==1:
            
            template = loader.get_template('cargar_imagen.html')
            modo_1 = ""
            modo_2 = "display:none"
            context={"modo_1":modo_1,"modo_2":modo_2}
            return HttpResponse(template.render(context,request))
            
        #return HttpResponseRedirect("principal")            
        #
    else:
        context={}
        return HttpResponse(template.render(context,request))