from django.db import models

# Create your models here.
class Number(models.Model):
    title    = models.CharField(max_length = 200)
    enteries = models.TextField()

    def __str__(self):
        return self.enteries
    

