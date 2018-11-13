from django.contrib import admin
from django.urls import path
from mdfiles.views import markdown_create, markdown_convert

urlpatterns = [
    path("markdown-create/", markdown_create, name="markdown-create"),
    path("markdown-convert/", markdown_convert, name="markdown-convert"),
]
