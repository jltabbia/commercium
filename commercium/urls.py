from django.contrib import admin
from django.urls import path,include
from .views import HomeView, cerrarSesion
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# from centroCosto import urls
# from conceptos import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/',cerrarSesion,name='salir'),
  #  path('centroCosto/',include('centroCosto.urls', namespace='centroCosto')),
  #  path('conceptos/',include('conceptos.urls', namespace='conceptos')),

]