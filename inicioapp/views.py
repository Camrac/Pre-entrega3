

# Create your views here.
from django.http import HttpResponse
from django.template import Template
from inicioapp.models import cafe
from django.shortcuts import render

def vista_cafe(request):
    return render(request,'inicio/index.html')




