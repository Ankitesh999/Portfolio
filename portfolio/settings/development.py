from .base import *

# Development: optionally load environment from .env for email and other sensitive vars
from pathlib import Path
import os
try:
    from dotenv import load_dotenv
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    ENV_PATH = BASE_DIR / '.env'
    if ENV_PATH.exists():
        load_dotenv(dotenv_path=ENV_PATH)
except Exception:
    pass

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Email configuration for development (use Gmail SMTP via .env when available)
import os as _os
EMAIL_HOST = _os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(_os.environ.get('EMAIL_PORT', '587'))
EMAIL_USE_TLS = _os.environ.get('EMAIL_USE_TLS', 'True').lower() in ('true', '1', 't')
EMAIL_HOST_USER = _os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = _os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = _os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
