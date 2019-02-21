from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from unidecode import unidecode
from django.template.defaultfilters import slugify


class OmeFile(models.Model):
    user = models.ForeignKey(User, default=1, null=True, verbose_name='User', on_delete=True, related_name='yazi')
    title = models.CharField(max_length=100, blank=False, null=True, verbose_name="Başlık giriniz: ",
                             help_text="Kaydetmek için başlık giriniz:")
    markdown_text = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Markdown yazı")
    created_date = models.DateField(auto_now_add=True, auto_now=False, null=True)
    slug = models.SlugField(null=True, unique=True, editable=False)

    class Meta:
        verbose_name_plural = "Gönderi"
        verbose_name = "Gönderiler"

    def __str__(self):
        return "title: {} text: {}".format(self.title, self.markdown_text)

    def get_absolute_url(self):
        return reverse('markdown-create')

    def get_unique_slug(self):
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while OmeFile.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "%s-%s" % (slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            omefile = OmeFile.objects.get(slug=self.slug)
            if omefile.title != self.title:
                self.slug = self.get_unique_slug()

        super(OmeFile, self).save(*args, **kwargs)
