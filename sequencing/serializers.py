from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'type')

class SampleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleType
        fields = ('id', 'name')

class SampleSerializer(serializers.ModelSerializer):
    run = serializers.SlugRelatedField(slug_field = 'name',
            queryset=Run.objects.all(), required = False)

    class Meta:
        model = Sample
        fields = ('id', 'date_modified', 'date_created', 'name', 'run', 'lane', 'description', 'index1',
        'index2', 'sample_type')
        read_only_fields = ('date_created', 'date_modified')

class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lane
        fields = ('id', 'number', 'run')

class RunSerializer(serializers.ModelSerializer):
    instrument = serializers.SlugRelatedField(slug_field = 'name',
            queryset=Instrument.objects.all())
    name = serializers.CharField(validators=[UniqueValidator(queryset=Run.objects.all())])
    run_samples = SampleSerializer(many=True, read_only=True)
    run_lanes = LaneSerializer(many=True, read_only=True)

    class Meta:
        model = Run
        fields = ('id', 'name', 'flowcell', 'lot', 'expiration', 'instrument',
        'date_created', 'date_modified', 'run_samples', 'run_lanes')
        read_only_fields = ('date_created', 'date_modified')

class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ('id', 'number', 'run', 'length', 'indexed')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'run', 'start_after', 'status', 'requestor')
        read_only_fields = ('date_created', 'date_modified')

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('id', 'request', 'analysis_type', 'cmd', 'start',
                'stop', 'code', 'pid', 'log')
        read_only_fields = ('date_created', 'date_modified')

class Bcl2fastqSampleAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bcl2fastqSampleAnalysis
        fields = ('id', 'analysis', 'sample', 'q30', 'cluster')
        read_only_fields = ('date_created', 'date_modified')
