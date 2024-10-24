from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Instrumento
from .serializer import InstrumentoSerializer
from django.views.generic import TemplateView
from django.shortcuts import render, redirect


# Esta clase es para que la API convierta el codigo a JSON.
class InstrumentoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer

#Pagina de inicio 
def inicio(request):
    return render(request, 'home.html')
