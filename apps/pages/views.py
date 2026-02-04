import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from apps.projects.models import Project


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    recent_projects = Project.objects.all()[:6]
    
    context = {
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    return render(request, 'pages/about.html')


def download_resume(request):
    """Serve the resume PDF file"""
    resume_path = os.path.join(settings.MEDIA_ROOT, 'Ankitesh_Tiwari_Resume.pdf')
    
    if not os.path.exists(resume_path):
        return HttpResponse("Resume not found".encode(), status=404, content_type='text/plain')
    
    with open(resume_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Ankitesh_Tiwari_Resume.pdf"'
        return response
