from .base import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblog-gigi108.c9users.io']

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}