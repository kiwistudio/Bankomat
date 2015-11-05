import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# sqlite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}