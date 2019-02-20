from django.contrib import admin
from django.urls import path
from .views import markdown_create, markdown_save, markdown_view, markdown_delete
from django.conf.urls import url

urlpatterns = [
    path("markdown-create/", markdown_create, name="markdown-create"),
    path("markdown-save/", markdown_save, name="markdown-save"),
    path("markdown-delete/<slug:slug>/", markdown_delete, name="markdown-delete"),
    path("markdown-view/<slug:slug>/", markdown_view, name="markdown-view"),

]
