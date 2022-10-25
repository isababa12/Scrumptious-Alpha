from django.contrib import admin
from tasks.models import Task

@admin.register(Task)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
    )
