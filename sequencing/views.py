from django.shortcuts import render
from rest_framework import generics
from .serializers import RunSerializer
from .models import Run

class RunCreate(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

    def perform_create(self, serializer):
        serializer.save()

class RunMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
