import random, string
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import urlShortener
from .serializers import urlShortenerSerializer

# Create your views here.
@api_view(['POST'])
def makeShortURL(request):
    data = request.data
    alphabet = string.ascii_lowercase + string.digits
    shorturl = ''.join(random.choices(alphabet, k=8))
    try:
        urlShortener.objects.create(
            longurl = data.longurl,
            shorturl = shorturl
        )
    except:
        shorturl = ''.join(random.choices(alphabet, k=8))
        urlShortener.objects.create(
            longurl = data.longurl,
            shorturl = shorturl
        )
    longurl = data['longurl']
    shorturl = "http://localhost:8000/"+shorturl
    
    return Response({'longurl': longurl, 'shorturl': shorturl})

def redirectUrl(request, shorturl):
    try:
        shortLink = urlShortener.objects.get(shorturl=shorturl)
    except urlShortener.DoesNotExist:
        shortLink = None

    if shortLink is not None:
        return Response(shortLink)