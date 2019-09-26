from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.db.models import Aggregate, CharField
import logging

class RequestList(ListView):
    model = Request

class RequestCreateForm(CreateView):
    model = Request
    fields = '__all__'

class RequestEditForm(UpdateView):
    model = Request
    fields = '__all__'

class RequestDetail(DetailView):
    model = Request

class SampleDetail(DetailView):
    model = Sample

class RunList(ListView):
    model = Run

class RunDetail(DetailView):
    model = Run

''' API VIEWS '''
class InstrumentCreate(generics.ListCreateAPIView):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer

    def perform_create(self, serializer):
        serializer.save()

class RunCreate(generics.ListCreateAPIView):
    queryset = Run.objects.all().prefetch_related('run_samples__sample_type')
    serializer_class = RunSerializer

    def perform_create(self, serializer):
        serializer.save()

class RunMod(generics.RetrieveUpdateDestroyAPIView):
    queryset = Run.objects.all()
    serializer_class = RunModSerializer
    lookup_field = 'name'

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

class GroupConcat(Aggregate):
    function = 'GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(expressions)s%(separator)s)'
    allow_distinct = True

    def __init__(self, expression, distinct=False, separator=None, **extra):
        output_field = extra.pop('output_field', CharField())
        distinct = 'DISTINCT ' if distinct else ''
        separator = " SEPARATOR '{}'".format(separator) if separator is not None else ''
        super(GroupConcat, self).__init__(
        expression, separator=separator, distinct=distinct, output_field=output_field, **extra)


class RunList(generics.ListAPIView):
    queryset = Run.objects.annotate(sample_types=GroupConcat('run_samples__sample_type', ', '))
    serializer_class = RunListSerializer
