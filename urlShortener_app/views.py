import random, string
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import urlShortener

# Create your views here.
@api_view(['POST'])
def makeShortURL(request):
    data = request.data['longurl']
    alphabet = string.ascii_lowercase + string.digits
    shorturl = ''.join(random.choices(alphabet, k=8))
    try:
        urlShortener.objects.create(
            longurl = data,
            shorturl = shorturl
        )
    except:
        return Response(data="bad request", status=status.HTTP_400_BAD_REQUEST)
    longurl = data
    shorturl = "http://localhost:8000/decode/"+shorturl
    
    return Response({'longurl': longurl, 'shorturl': shorturl})

def redirectUrl(request, shorturl):
    try:
        shortLink = urlShortener.objects.get(shorturl=shorturl)
    except urlShortener.DoesNotExist:
        shortLink = None

    if shortLink is not None:
        return Response(shortLink)