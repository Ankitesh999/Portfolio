import os

ALLOWED_HOSTS = [
    ".onrender.com",
]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.development')
