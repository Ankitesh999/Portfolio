import os

ALLOWED_HOSTS = [
    ".onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.development')
