from operator import truediv
from django.db import models

# Create your models here.
class urlShortener(models.Model):
    long_url = models.URLField(max_length=300, unique=True)
    short_url = models.URLField(max_length=300, unique=True)
    
    def __str__(self):
        return self.short_url