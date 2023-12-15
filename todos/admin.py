from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'completed_count')
    readonly_fields = ('completed_count',)

    def completed_count(self, obj):
        return Todo.objects.filter(completed=True).count()
    completed_count.short_description = 'Completed Tasks Count'

admin.site.register(Todo, TodoAdmin)
