from django.db import models

# Create your models here.
class ImageGallery(models.Model):
    title=models.CharField(max_length=100,default="title")
    description=models.CharField(max_length=255,default="lorem epsum")
    Images=models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title