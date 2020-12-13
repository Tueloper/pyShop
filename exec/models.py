from django.db import models


# Create your models here.
class Exec(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    discount = models.FloatField()



