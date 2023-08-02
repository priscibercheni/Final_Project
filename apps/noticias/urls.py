
from django.urls import path
from . import views
from .views import  CrearPosteo, listar_NoticiasArte, deletecomment, listar_NoticiasTurismo


app_name='noticias'
urlpatterns = [
    path('arte' , listar_NoticiasArte, name='listararte.html'),
    path('turismo' , listar_NoticiasTurismo, name='listarturismo.html'),
    path("agregar_posteo/", CrearPosteo.as_view(), name="agregar_posteo"),
    path('post/<int:pk>/', views.post_detail, name='detallenoticias'),
    path('comment/<int:id>/', deletecomment, name='socio_comment'),
]
