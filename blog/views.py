from django.shortcuts import render
from apps.noticias.models import Post
from apps.eventos.models import Eventos
from django.urls import path
from . import views


def Home(request):
    posts = Post.objects.all().order_by('-fecha')[:2]
    return render(request, 'Home.html', {'ultima_noticias': posts})


def quienes_somos(request):
    return render(request, 'quienes_somos.html')


def nombre_de_la_vista(request):
    # Lógica de la vista
    return render(request, 'ruta/a/template.html')


def lista_noticias(request):
    posts = Post.objects.all().order_by('-fecha')[:2]
    return render(request, 'noticias/lista_noticias.html', {'post_noticias': posts})

def lista_eventos(request):
    eventos = Eventos.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'post_eventos': eventos})