from django.db import models


# Create your models here.


class Asset(models.Model):
    Asset = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
