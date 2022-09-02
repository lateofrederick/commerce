from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-dfyqbmfsjm#pnc#bmie#tce58bdlw1n%7jr!c!dgrbwhl6gqf('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store',
        'USER': 'admin',
        'PASSWORD': 'store123user',
        'HOST': 'localhost',
        'PORT': '',
    }
}
