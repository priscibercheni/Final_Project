from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Eventos

# Create your views here.

def listar_Eventos(request):
    evento = Eventos.objects.all().order_by('-fecha')
    return render(request, 'eventos/listareventos.html', { 'post_eventos': evento})

