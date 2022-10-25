from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required


@login_required
def projects_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects_list": projects,
    }
    return render(request, "projects/list.html", context)
