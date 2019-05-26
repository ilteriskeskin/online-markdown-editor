from django import forms
from .models import OmeFile


class OmeForm(forms.ModelForm):
    class Meta:
        model = OmeFile
        fields = ['title', 'markdown_text']

    def __init__(self, *args, **kwargs):
        super(OmeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}

        kwargs.update({"widget": forms.Textarea})
        self.fields['markdown_text'].widget.attrs = {'id': 'mdyazi',
                                                     'class': 'content',
                                                     'url': '{% url "markdown-create" %}',
                                                     'placeholder': ">>"
                                                     }
