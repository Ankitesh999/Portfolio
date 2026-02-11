import os
import dj_database_url
from pathlib import Path
from .base import *
from dotenv import load_dotenv

# Load environment variables from .env if present (local development)
BASE_DIR_PATH = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR_PATH / '.env'
try:
    load_dotenv(dotenv_path=ENV_PATH)
except Exception:
    pass

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise Exception("SECRET_KEY is missing in environment variables")

ALLOWED_HOSTS = [
    ".onrender.com",  # allow all Render preview/production subdomains
    "portfolio-iawd.onrender.com",
    "portfolio-pr-1.onrender.com",
    "portfolio-pr-1-side.onrender.com",
    "ankiteshtiwari.in",
    "www.ankiteshtiwari.in",
]

DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# Static files for production
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files for production
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Serve media files in production via Django (for small files like resume)
# Note: For production with many media files, use proper file storage service

# Security settings for production
SECURE_SSL_REDIRECT = False  # Platform handles HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_SECONDS = 0
CSRF_TRUSTED_ORIGINS = [
    "https://portfolio-iawd.onrender.com",
    "https://portfolio-pr-1.onrender.com",
    "https://portfolio-pr-1-side.onrender.com",
    "https://ankiteshtiwari.in",
    "https://www.ankiteshtiwari.in",
]

# Email settings
# Email configuration
# Provide sensible defaults for free Gmail SMTP on Render or similar hosting.
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True')
try:
    EMAIL_USE_TLS = EMAIL_USE_TLS.lower() in ('true', '1', 't')
except Exception:
    EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# If a default from email isn't provided, fall back to the host user when available
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
