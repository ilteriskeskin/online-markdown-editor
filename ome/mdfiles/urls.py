from django.contrib import admin
from django.urls import path
from mdfiles.views import markdown_create, markdown_save

urlpatterns = [
    path("markdown-create/", markdown_create, name="markdown-create"),
    #path("markdown-convert/", markdown_convert, name="markdown-convert"),
    path("markdown-save/", markdown_save, name="markdown-save")
]
