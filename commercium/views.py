from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from empresa.models import Empresa
from static import globales

# Create your views here.
@login_required()

def HomeView(request): 
    empresa = Empresa.objects.raw("SELECT empresa.* FROM empresa")
    context= {
        'emp' : empresa,
    }
    return render(request,'index.html',context)
    #return render(request,'index.html')

def cerrarSesion(request):
    logout(request)
    return redirect('index')