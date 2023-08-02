from django import forms


from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={ 'class': 'form-control'}),label='Correo', required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}), label='Nombre', required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}), label='Nombre de Usuario', required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'form-control'}),label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput(attrs={ 'class': 'form-control'}), required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={ 'class': 'form-control'}), required=True)

    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
