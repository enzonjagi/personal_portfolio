from django.shortcuts import render
from .models import Project

def project_index(request):
    """Renders a Template for the Project App's index page"""

    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    """A view of individual projects on the Showcase app"""

    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)