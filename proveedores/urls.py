from django.urls import path, re_path
from .views import ProveedorHomeView, AgregarProveedor, editarProveedor, eliminarProveedor

app_name='proveedores'

urlpatterns = [
    path('', ProveedorHomeView, name='index'),
    path('agregar',AgregarProveedor.as_view(),name="agregar"),
    path('eliminar', eliminarProveedor, name='eliminar'),
    path('editar', editarProveedor, name='editar'),
    
]