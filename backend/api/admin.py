from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.site_title = 'Админ-зона Taski.'
admin.site.site_header = 'Админ-зона Taski.'
