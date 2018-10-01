from django.contrib import admin

from .models import Files

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):

    list_display = ["name","files"]

    list_display_links = ["name","files"]

    
    class Meta:
        model = Files