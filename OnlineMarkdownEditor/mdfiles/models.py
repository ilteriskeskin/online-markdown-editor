from django.db import models

class Files(models.Model):
    name = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı", blank = True, null = True)
    files = models.CharField(verbose_name ="Dosya",max_length=50, blank = True, null = True)

    def __str__(self):
        return self.files
