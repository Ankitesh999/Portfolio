# Django Portfolio Website

A clean, professional portfolio website built with Django, HTMX, and Tailwind CSS.

## Features

- **Backend**: Django 4.2 LTS with modular app structure
- **Frontend**: Tailwind CSS + HTMX for enhanced UX
- **Database**: PostgreSQL ready (SQLite for development)
- **Admin**: Full Django admin interface
- **Production Ready**: Proper dev/prod settings split, static files handled by Whitenoise

## Project Structure

```
portfolio/
├── portfolio/              # Main Django project
│   ├── settings/          # Dev/prod settings split
│   └── wsgi.py
├── apps/                  # Django apps
│   ├── pages/            # Home, about pages
│   ├── projects/         # Project showcase
│   └── contact/          # Contact form
├── templates/            # Base templates & components
├── static/              # CSS, JS, images
└── media/               # User uploads
```

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Start development server:
   ```bash
   python manage.py runserver
   ```

5. Visit http://localhost:8000

## Admin Interface

Access the admin at http://localhost:8000/admin to manage:
- Projects (with image uploads)
- Contact messages
- Content management

## Deployment

The app is production-ready with:
- Environment variable configuration
- Proxy-aware security settings
- Static file handling with Whitenoise
- PostgreSQL configuration for production

## Customization

- Edit `templates/base.html` for branding
- Update `templates/pages/home.html` for hero section
- Add projects via Django admin or admin interface
- Customize colors in Tailwind config

## Tech Stack

- Django 4.2 LTS
- Tailwind CSS (via CDN)
- HTMX 1.9.10
- PostgreSQL (production)
- Whitenoise (static files)
- Pillow (image handling)