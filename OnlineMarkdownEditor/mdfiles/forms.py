from .models import Files

from django import forms



class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ["files"]