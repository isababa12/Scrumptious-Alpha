from django.shortcuts import render
from .models import Project


def projects_list(request):
    projects = Project.objects.all()
    context = {
        "projects_list": projects,
    }
    return render(request, "projects/list.html", context)
