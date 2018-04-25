from django.shortcuts import render
from rest_framework import generics
from .serializers import RunSerializer
from .models import Run

class Create(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

    def perform_create(self, serializer):
        serializer.save()
