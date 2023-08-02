from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from apps.usuarios.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        #return reverse('detalle_posteo', args=(str(self.id,)))
        return reverse('home')
        
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(blank=True, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='static/img/')
    fecha = models.DateTimeField(auto_now_add=True) 
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    # autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        #return reverse('detalle_posteo', args=(str(self.id,)))
        return reverse('Home')

class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comentarios')
	user=models.ForeignKey(Usuario,on_delete=models.CASCADE)
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'comentario on {} por {}'.format(self.post.titulo,self.user.username)

