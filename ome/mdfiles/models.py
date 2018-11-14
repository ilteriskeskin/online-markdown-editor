from django.db import models

import markdown2


# Create your models here.


class OmeFile(models.Model):
    markdown_text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Markdown yazı")
    html_text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="HTML yazı")

    class Meta:
        verbose_name_plural = "Gönderi"
        verbose_name = "Gönderiler"

    def __str__(self):
        return "{} {}".format(self.markdown_text, self.html_text)



