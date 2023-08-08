
from django.urls import include
from django.contrib import admin
from django.urls import path

from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType

from blog import urls as blog_urls


admin.site.register(AbstractUser)
admin.site.register(ContentType)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'mysite.urls'
ALLOWED_HOSTS = ['narafinoss.pythonanywhere.com']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog_urls)),
]



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


from pathlib import Path
import os
from django.urls import reverse_lazy


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*o=cks(^0cr%*-j96@b%y78k^&$1=gg^9=p1tkyzk5s452pl1^'

AUTH_USER_MODEL = 'usuarios.usuario'

LOGIN_REDIRECT_URL = reverse_lazy('Home')
LOGOUT_REDIRECT_URL = reverse_lazy('Home')
LOGIN_URL = reverse_lazy('login')




# Application definition

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#         {
#             'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#         },
#         {
#             'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#         },
#         {
#             'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#         },
#         {
#             'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#         },
#     ]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static'),)


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
