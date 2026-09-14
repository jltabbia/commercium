
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Proveedores
from empresa.models import Empresa  
from static import globales

import datetime 
import decimal

def ProveedorHomeView(request):
    
    #pro=Proveedores.objects.raw("SELECT * FROM proveedores")
    empresa=Empresa.objects.raw("SELECT * FROM empresa")
    
    
    context={
     #   'Proveedores' : pro,
        'emp' : empresa,
    }
    return render(request,'proveedores/index.html',context)

class ProveedorView(View):
    def get(self,request,*args,**kwargs):
        proveedor=Proveedores.objects.raw("SELECT * FROM proveedores")
        empresa=Empresa.objects.raw("SELECT * FROM empresa")
        
        context={
            'Proveedores' : proveedor,
            'emp' : empresa,
        }
        return render(request,'proveedores/proveedor.html',context)
    
class AgregarProveedor(View):
        
    def post(self,request,*args,**kwargs):
        proveedor=Proveedores()
        proveedor.codigo=request.POST.get('codigo')
        proveedor.nombre=request.POST.get('nombre').upper()
        proveedor.domicilio=request.POST.get('domicilio').upper()
        proveedor.provincia=request.POST.get('provincia')
        proveedor.localidad=request.POST.get('localidad')
        
        proveedor.save()
        return redirect('proveedores:index')

def editarProveedor(request):
    id=request.POST.get('id')
    proveedor=Proveedores.objects.get(id=id) 

    proveedor.codigo=request.POST.get('cod')
    proveedor.nombre=request.POST.get('nom').upper()
    proveedor.domicilio=request.POST.get('domicilio').upper()
    proveedor.provincia=request.POST.get('provincia')
    proveedor.localidad=request.POST.get('localidad')
    
    proveedor.save()
            
    return redirect('proveedores:index')

def eliminarProveedor(request):
    id=request.POST.get('id1')
    proveedor=Proveedores.objects.get(id=id)
    proveedor.delete()
        
    return redirect('proveedores:index')