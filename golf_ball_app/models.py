from django.db import models

# Create your models here.
class Golf_Ball(models.Model):
    brand = models.CharField(max_length=100)
  