from django.urls import path
from .views import create, draw

urlpatterns = [
    path('', create, name = 'create'),
    path('draw/', draw, name = 'draw')
]
