from django.contrib import admin
from django.urls import path
from .views import markdown_create, markdown_delete
from django.conf.urls import url

urlpatterns = [
    path("markdown-create/", markdown_create, name="markdown-create"),
    path("markdown-create/<slug:slug>/", markdown_create, name="markdown-create"),
    path("markdown-delete/<slug:slug>/", markdown_delete, name="markdown-delete"),

]
