"""Tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recomendacion.views import Resultado, Post, Precision, Estadistica, likes
from django.conf import settings
from django.conf.urls.static import static
#from recomendacion.models import Preguntas

#Se definen las rutas de la api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('recomendacion.urls')),
    path('Resultado', Resultado, name="Resultado"),
    path('Estadistica', Estadistica, name="Estadistica"),
    path('Post', Post, name="Post"),
    path('Pre', Precision, name="Pre"),
    path('likes', likes, name="likes"),
    #path('api/v2.0/', include('Preguntas.urls')),
] 

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)