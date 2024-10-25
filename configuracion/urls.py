"""
URL configuration for configuracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

#Librerias por defecto de Django
from django.contrib import admin
from django.urls import path, include

#Aqui estoy utilizando la libreria coreapi para mas documentacion
from rest_framework.documentation import include_docs_urls

from api import views

#Aqui estoy utilizando la libreria JWT para mas seguridad por Tokens

urlpatterns = [
    #Estas son mis urls, el name significado como se van a visualizar en el navegador
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('docs/', include_docs_urls(title='Documentacion'),  name='api-docs'),
]
