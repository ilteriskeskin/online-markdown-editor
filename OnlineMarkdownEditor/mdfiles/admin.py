from django.contrib import admin

from .models import Files, ConvertFile

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):

    list_display = ["name","files"]

    list_display_links = ["name","files"]

    
    class Meta:
        model = Files

@admin.register(ConvertFile)
class ConvertFile(admin.ModelAdmin):

    list_display = ["files"]

    list_display_links = ["files"]

    
    class Meta:
        model = ConvertFile