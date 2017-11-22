import dj_database_url


print('-------- Production settings have been loaded. --------')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Allow all host headers
ALLOWED_HOSTS = ['emozioni.herokuapp.com']
