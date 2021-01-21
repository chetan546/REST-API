from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255,default=True)
    email = models.CharField(max_length=255,default=True)
    image = models.ImageField(default=True)

    def __str__(self):
        return self.name
