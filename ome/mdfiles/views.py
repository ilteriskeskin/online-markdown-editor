from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse

from .models import OmeFile
from .forms import OmeForm

import markdown2


def markdown_create(request, slug=None):
    data = {'markdown_text': ''}
    if request.is_ajax():
        if request.method == 'POST':
            gelen = request.POST.get('markdown_text')
            html_text = markdown2.markdown(gelen)
            data.update({'markdown_text': html_text})
            return JsonResponse(data=data, safe=False)

    form = OmeForm(data=request.POST or None)
    mdfile = OmeFile.objects.all()

    if form.is_valid():
        if 'save' in request.POST:
            baslik = form.cleaned_data.get('title')
            if OmeFile.objects.filter(title=baslik).exists():
                omefile = get_object_or_404(OmeFile, title=baslik)
                form = OmeForm(instance=omefile, data=request.POST or None)
                if form.is_valid():
                    form.save()
            else:
                gelen = request.POST.get('markdown_text')
                html_text = markdown2.markdown(gelen)
                new_ome = form.save(commit=True)
                new_ome.html_text = html_text
                new_ome.user = request.user
                new_ome.save()

    if slug:
        omefile = get_object_or_404(OmeFile, slug=slug)
        form = OmeForm(instance=omefile, data=request.POST or None)
        return render(request, 'markdown_convert.html', context={'slug': slug, 'form': form, 'omefile': omefile})

    return render(request, 'markdown_convert.html', context={'form': form, 'mdfile': mdfile})


def markdown_delete(request, slug):
    omefile = get_object_or_404(OmeFile, slug=slug)
    omefile.delete()
    return HttpResponseRedirect(reverse('markdown-create'))
