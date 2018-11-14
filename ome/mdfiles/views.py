from django.shortcuts import render, get_object_or_404
from .models import OmeFile
from .forms import OmeForm

import markdown2


# Create your views here.

def markdown_create(request):
    form = OmeForm()
    mdfile = OmeFile.objects.all()
    return render(request, 'markdown_convert.html', context={'form': form, 'mdfile': mdfile})


def markdown_convert(request):
    mdfile = OmeFile.objects.all()
    if request.method == "POST":
        form = OmeForm(data=request.POST)
        if form.is_valid():
            new_ome = form.save(commit=False)
            markdown_text = form.cleaned_data.get('markdown_text')
            new_ome.html_text = markdown2.markdown(markdown_text)
            new_ome.save()
        return render(request, 'markdown_convert.html', context={'form': form, 'mdfile': mdfile})
