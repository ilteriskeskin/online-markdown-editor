from django.shortcuts import render
from .models import Files
from .forms import FileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import ConvertFile
import markdown2 

# Create your views here.

@login_required(login_url = "user:login")
def createfiles(request):

    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        files = form.save(commit=False)

        #files.author = request.user
        files.save()


        return render(request,"index.html")

    return render(request,"addfiles.html",{"form":form})

def fileconvert(request):
    a = markdown2.markdown(ConvertFile.convertfiles)
    a.save()
    return render(request,"fileview.html",{"a":a})


def fileview(request):
    file = Files.objects.all()
    return render(request, "fileview.html", {"file":file})
