import os
import dj_database_url
from .base import *


env = os.environ.copy()

SECRET_KEY = env['SECRET_KEY']
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
DEBUG = False

try:
   from .local import *
except ImportError:
   pass

heroku config:set SECRET_KEY=mcGH7AE1b2MMuJOMN2R70Mvo2VQVWhw5th84quWK8LHL2D8w9g ALLOWED_HOSTS=abigail-site.herokuapp.com PRIMARY_HOST=abigail-site.herokuapp.com -a abigail-site

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'