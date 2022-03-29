from django.contrib import admin
from todoapp.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "description", "priority", "created_at")


admin.site.register(Todo, TodoAdmin)