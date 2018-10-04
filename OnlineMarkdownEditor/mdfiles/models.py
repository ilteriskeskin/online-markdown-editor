from django.db import models
import markdown2




class Files(models.Model):

    
    name = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı")
    files = models.TextField(verbose_name ="Dosya",max_length = 50)
    

    def __str__(self):
        return self.files

class ConvertFile(models.Model):
    files = models.ForeignKey(Files, on_delete = models.CASCADE,verbose_name="convertfile")
    def convert(files):
        files = (str)(files)
        convertfiles = markdown2.markdown(files)
        return convertfiles

    convertfiles = convert(files)
    
    def __str__(self):
        return self.convertfiles 
