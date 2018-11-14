from django import forms
from .models import OmeFile


class OmeForm(forms.ModelForm):
    class Meta:
        model = OmeFile
        fields = ['markdown_text']
