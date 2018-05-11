from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'type')

class RunSerializer(serializers.ModelSerializer):
    instrument = serializers.SlugRelatedField(slug_field = 'name',
            queryset=Instrument.objects.all())
    name = serializers.CharField(source='run.name', validators=[UniqueValidator(queryset=Run.objects.all())])

    class Meta:
        model = Run
        fields = ('id', 'name', 'flowcell', 'lot', 'expiration', 'instrument')
        read_only_fields = ('date_created', 'date_modified')

class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lane
        fields = ('id', 'number', 'run')

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'name', 'run', 'lane', 'description', 'index1',
        'index2')
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
