from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post,Comment
from .forms import PosteoForm, Post, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


class CrearPosteo(CreateView):
    model = Post
    form_class = PosteoForm
    template_name = 'noticias/agregar_post.html'
    #fields = '__all__'
    #fields = ['titulo', 'contenido']
    def get_success_url(self) -> str:
        return reverse_lazy('home.html')

def listar_NoticiasArte(request):
    posts = Post.objects.all().filter(categoria=1)
    post_ordenados = posts.order_by('-fecha')
    return render(request, 'noticias/listararte.html', { 'post_noticias': post_ordenados})

def listar_NoticiasTurismo(request):
    posts = Post.objects.all().filter(categoria=2)
    post_ordenados = posts.order_by('-fecha')
    return render(request, 'noticias/listarturismo.html', { 'post_noticias': post_ordenados})

@login_required  
def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    ied=pk
    comments=Comment.objects.filter(post=post).order_by("-pk")
    
    if request.method == 'POST':
            cf=CommentForm(request.POST or None)
            if cf.is_valid():
                content=request.POST.get('content')
                comment=Comment.objects.create(post=post,user=request.user,content=content)
                comment.save()
                return redirect('/')
    else:
        cf=CommentForm()
        
    context={
            'titulo': 'Post Details',
            'comments':comments,
            'ied':ied,
            'object':post,
            'comment_form':cf
    }
    return render(request,'noticias/detallenoticias.html',context)

@login_required
def deletecomment(request, id):
    comment=get_object_or_404(Comment,id=id)
    comment.delete()
    messages.success(request,f'Comentario borrado!')
    return redirect('/')
