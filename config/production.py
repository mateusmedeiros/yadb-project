from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    # Production hostname(s) goes here    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'prod.db.sqlite3'),
    }
}

