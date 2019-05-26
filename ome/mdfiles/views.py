from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse

from .models import OmeFile
from .forms import OmeForm

import markdown2


def markdown_create(request, slug=None):
    data = {'markdown_text': '', 'title': ''}
    form = OmeForm(data=request.POST or None)

    if request.is_ajax():

        if request.method == 'POST':

            if request.POST.get('status') == 'save':

                baslik = request.POST.get('title')

                if OmeFile.objects.filter(title=baslik).exists() and request.user == OmeFile.user:
                    omefile = get_object_or_404(OmeFile, title=baslik)
                    form = OmeForm(instance=omefile, data=request.POST or None)
                    if form.is_valid():
                        form.save()
                else:
                    gelen = request.POST.get('markdown_text')
                    html_text = markdown2.markdown(gelen)
                    new_ome = form.save(commit=True)
                    new_ome.title = baslik
                    new_ome.markdown_text = html_text
                    new_ome.user = request.user
                    new_ome.save()

            else:
                gelen = request.POST.get('markdown_text')
                html_text = markdown2.markdown(gelen)
                data.update({'markdown_text': html_text})
                return JsonResponse(data=data, safe=False)

    mdfile = OmeFile.objects.all()

    if slug:
        omefile = get_object_or_404(OmeFile, slug=slug)
        form = OmeForm(instance=omefile, data=request.POST or None)
        return render(request, 'markdown_convert.html', context={'slug': slug, 'form': form, 'omefile': omefile})

    return render(request, 'markdown_convert.html', context={'form': form, 'mdfile': mdfile})


def markdown_delete(request, slug):
    omefile = get_object_or_404(OmeFile, slug=slug)
    omefile.delete()
    return HttpResponseRedirect(reverse('markdown-create'))
