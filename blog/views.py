from django.shortcuts import render
from apps.noticias.models import Post

def Home (request):
    posts = Post.objects.all().order_by('-fecha')[:2]
    return render( request, 'Home.html', { 'ultima_noticias': posts})

def Quienes (request):
    return render( request, 'Quienes.html')


