

# Create your views here.
from django.http import HttpResponse
from django.template import Template
from inicioapp.models import cafe
from django.shortcuts import render

    


def vista_cafe(request):
    return render(request,'inicio/index.html')


def historia_del_cafe (request):
 return render(request,'inicioapp/templates/inicio/historia_del_cafe.html')


def tipo_de_cafe(request):
    return render(request,'inicioapp/templates/inicio/tipos_de_cafe.html')


def about_me(request):
    return render (request,'inicioapp/templates/inicio/about_me.html')


def home(request):
    return render(request,'inicioapp/templates/inicio/home.html')