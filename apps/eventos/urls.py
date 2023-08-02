from django.urls import path
from . import views
from .views import  listar_Eventos


app_name='eventos'
urlpatterns = [
    path('' , listar_Eventos, name='listareventos.html'),
]