from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    return render(request, 'projects/list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    context = {
        'project': project,
    }
    return render(request, 'projects/detail.html', context)
