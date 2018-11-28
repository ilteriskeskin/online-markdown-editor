from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class OmeFile(models.Model):
    user = models.ForeignKey(User, default=1, null=True, verbose_name='User', on_delete=True, related_name='yazi')
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name="Başlık giriniz: ",
                             help_text="Kaydetmek için başlık giriniz:")
    markdown_text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Markdown yazı")
    html_text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="HTML yazı")
    created_date = models.DateField(auto_now_add=True, auto_now=False, null=True)

    class Meta:
        verbose_name_plural = "Gönderi"
        verbose_name = "Gönderiler"

    def __str__(self):
        return "{} {}".format(self.markdown_text, self.html_text)

    def get_absolute_url(self):
        return reverse('markdown-create')
