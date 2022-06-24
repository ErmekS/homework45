from django.contrib import admin

# Register your models here.
from webapp.models import Sketchpad


class SketchpadAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'created_note', 'date_of_completion']
    list_display_links = ['description']
    list_filter = ['status']
    search_fields = ['status']
    fields = ['description', 'status', 'created_note', 'date_of_completion']
    readonly_fields = ['created_note', 'date_of_completion']


admin.site.register(Sketchpad, SketchpadAdmin)
