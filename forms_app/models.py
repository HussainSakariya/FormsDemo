from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=5)

class add_image(models.Model):
    name=models.CharField(max_length=20)
    img=models.ImageField(upload_to="img")

