from django.db import models

# Create your models here.
class Image(models.Model):
    uploader=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.uploader