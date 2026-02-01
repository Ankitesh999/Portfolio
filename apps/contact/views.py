from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            form = ContactForm()  # Reset form after successful submission
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/form.html', context)
