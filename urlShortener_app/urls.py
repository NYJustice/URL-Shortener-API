from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.makeShortURL),
    path('decode/<str:shorturl>', views.redirectUrl),
]