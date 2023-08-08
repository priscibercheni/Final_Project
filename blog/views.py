from django.shortcuts import get_object_or_404, render
from apps.noticias.models import Comment, Post
from apps.eventos.models import Eventos
from django.urls import path
from apps.noticias.forms import CommentForm
from apps.noticias.views import post_detail

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

def evento(request, pk):
    obj_evento = get_object_or_404(Eventos, pk=pk)
    context = {
        'evento': obj_evento
    }
    return render(request, 'eventos/evento.html', context)

def noticia(request, id_noticia):
    comment_form = CommentForm
    noticia = get_object_or_404(Post, pk=id_noticia)

    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                post=post_detail, user=request.user, content=content)
            comment.save()
            return redirect('/')
    else:
        cf = CommentForm()

    context = {
        'titulo': 'Post Details',
        'comment_form': cf,
        'noticia': noticia
    }

    return render(request, 'noticias/noticia.html', context)


def añadir_comentario(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_id = request.POST.get('post_id')
            comment = comment_form.save(commit=False)
            comment.post_id = post_id
            comment.save()
            return redirect('noticias/lista_noticias.html')
        else:
            comment_form = CommentForm()
