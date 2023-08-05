
from.base import*

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'libreria',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',   # Puedes cambiarlo si tu base de datos está en un servidor remoto
        'PORT': '3306',            # El puerto de la base de datos (por defecto: 3306)
    }
}
