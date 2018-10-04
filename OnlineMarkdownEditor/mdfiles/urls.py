from django.contrib import admin
from django.urls import path,include
from . import views

app_name ="mdfiles"

urlpatterns =[
    path('createfiles/',views.createfiles,name="createfiles"),
    path('fileview/', views.fileview, name="fileview"),
    path('fileconvert/', views.fileconvert, name="fileconvert"),
]
