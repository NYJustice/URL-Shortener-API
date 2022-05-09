from django.contrib import admin
from urlShortener_app.models import urlShortener

# Register your models here.
@admin.register(urlShortener)
class urlShortenerAdmin(admin.ModelAdmin):
    pass