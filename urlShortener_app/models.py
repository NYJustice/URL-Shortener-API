from django.db import models
from django.forms import URLField

# Create your models here.
class urlShortener(models.Model):
    longurl = models.URLField(max_length=300, unique=True)
    shorturl = models.CharField(max_length=300, unique=True, default=None)
    
    def __str__(self):
        return self.shorturl