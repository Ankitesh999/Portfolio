from django.shortcuts import render
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
