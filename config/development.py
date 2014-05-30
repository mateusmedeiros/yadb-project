from .base import *

ROOT_URLCONF = 'urls.development'

DEBUG = True
TEMPLATE_DEBUG = True

# No cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db.sqlite3'),
    }
}
