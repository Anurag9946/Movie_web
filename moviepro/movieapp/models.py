from django.db import models

# Create your models here.

class Movies( models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

class Sports( models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery1')

    def __str__(self):
        return self.name
























