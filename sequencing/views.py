from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


''' API VIEWS '''
class InstrumentCreate(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

    def perform_create(self, serializer):
        serializer.save()

class RunTypeCreate(generics.ListCreateAPIView):
    queryset = RunType.objects.all()
    serializer_class = RunTypeSerializer

    def perform_create(self, serializer):
        serializer.save()

class RunCreate(generics.ListCreateAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

    def perform_create(self, serializer):
        serializer.save()

class RunMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Run.objects.all()
    serializer_class = RunSerializer

class LaneCreate(generics.ListCreateAPIView):
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer

    def perform_create(self, serializer):
        serializer.save()

class LaneMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lane.objects.all()
    serializer_class = LaneSerializer

class SampleCreate(generics.ListCreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    def perform_create(self, serializer):
        serializer.save()

class SampleMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class ReadCreate(generics.ListCreateAPIView):
    queryset = Read.objects.all()
    serializer_class = ReadSerializer

    def perform_create(self, serializer):
        serializer.save()

class ReadMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Read.objects.all()
    serializer_class = ReadSerializer

class RequestCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save()

class RequestMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class AnalysisCreate(generics.ListCreateAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

    def perform_create(self, serializer):
        serializer.save()

class AnalysisMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer

class Bcl2fastqSampleAnalysisCreate(generics.ListCreateAPIView):
    queryset = Bcl2fastqSampleAnalysis.objects.all()
    serializer_class = Bcl2fastqSampleAnalysisSerializer

    def perform_create(self, serializer):
        serializer.save()

class Bcl2fastqSampleAnalysisMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bcl2fastqSampleAnalysis.objects.all()
    serializer_class = Bcl2fastqSampleAnalysisSerializer
