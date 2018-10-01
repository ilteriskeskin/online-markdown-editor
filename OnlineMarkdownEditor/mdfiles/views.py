from django.shortcuts import render
from .models import Files
from .forms import FileForm

# Create your views here.

def createfiles(request):

    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        files = form.save(commit=False)
        
        files.author = request.user
        files.save()

    
        return render(request,"index.html")

    return render(request,"addfiles.html",{"form":form})
