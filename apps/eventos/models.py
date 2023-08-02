from django.db import models
from django.urls import reverse

# Create your models here.
class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(blank=True, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='static/img/')
    fecha = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        #return reverse('detalle_posteo', args=(str(self.id,)))
        return reverse('home')