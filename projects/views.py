from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


@login_required
def projects_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects_list": projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    projects = get_object_or_404(Project, id=id)
    context = {
        "project_details": projects,
    }
    return render(request, "projects/details.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
        }
    return render(request, "projects/create.html", context)
