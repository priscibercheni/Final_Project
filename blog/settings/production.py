import os
from pathlib import Path

SECRET_KEY = 'django-insecure-*o=cks(^0cr%*-j96@b%y78k^&$1=gg^9=p1tkyzk5s452pl1^'

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['narafinoss.pythonanywhere.com']

BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DATABASES = {
 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'narafinoss$proyectofinal',
        'USER': 'narafinoss',
        'PASSWORD': 'rserRS200clN',
        'HOST': 'narafinoss.mysql.pythonanywhere-services.com',   # Puedes cambiarlo si tu base de datos está en un servidor remoto
        'PORT': '3306',            # El puerto de la base de datos (por defecto: 3306)
    }
}
ROOT_URLCONF = 'blog.urls'

# Media files (User uploaded files)
MEDIA_ROOT = '/home/narafinoss/repo_final/static/img'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '/home/narafinoss/repo_final/templates')],
        'APP_DIRS': True,
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.usuarios',
    'apps.noticias',
    'apps.eventos',
    'ckeditor',
]

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/narafinoss/repo_final/logfile.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

STATIC_URL = '/static/'

STATIC_ROOT = "/home/narafinoss/repo_final/static"
# or, eg,


