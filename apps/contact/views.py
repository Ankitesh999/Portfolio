from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import logging
from .models import ContactMessage
from .forms import ContactForm


logger = logging.getLogger(__name__)


def contact_form(request):
    mail_sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to DB first so we have a timestamp and data to email
            contact = form.save()

            # Build email content
            subject = f"New contact form submission: {contact.subject}"
            message = (
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Subject: {contact.subject}\n\n"
                f"Message:\n{contact.message}\n\n"
                f"Timestamp: {contact.timestamp}"
            )
            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None)
            recipient_list = ['official.ankitesh@gmail.com']
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                mail_sent = True
            except (Exception, SystemExit) as e:
                # Do not crash the user flow; log the error for troubleshooting
                logger.exception("Failed to send contact form email: %s", e)
                mail_sent = False

            if mail_sent:
                from django.contrib import messages as django_messages
                django_messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            else:
                from django.contrib import messages as django_messages
                django_messages.warning(request, 'Thanks for reaching out. We could not email this submission right now; we saved it locally and will follow up manually.')

            form = ContactForm()  # Reset form after handling
            # If the request is an HTMX request, return only the partial form to swap in
            if request.headers.get('Hx-Request') or request.headers.get('HX-Request'):
                from django.template.loader import render_to_string
                html = render_to_string('contact/form_partial.html', {'form': form}, request=request)
                return HttpResponse(html)
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    # On normal GET (not HTMX), render the full page
    if request.headers.get('Hx-Request') or request.headers.get('HX-Request'):
        from django.template.loader import render_to_string
        html = render_to_string('contact/form_partial.html', {'form': form}, request=request)
        return HttpResponse(html)
    return render(request, 'contact/form.html', context)
