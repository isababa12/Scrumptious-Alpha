from django.contrib import admin
from .models import Project


@admin.register(Project)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
