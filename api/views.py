from django.shortcuts import render

# Create your views here.
# artists/views.py

from rest_framework import viewsets
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
