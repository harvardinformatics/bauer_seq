from rest_framework import serializers
from .models import *

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'type')

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'name', 'flowcell', 'lot', 'expiration', 'instrument_id')
        read_only_fields = ('date_created', 'date_modified')

class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lane
        fields = ('id', 'lane_num', 'run_id')

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'name', 'run_id', 'lane_id', 'description', 'index1',
        'index2')
        read_only_fields = ('date_created', 'date_modified')

class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ('id', 'number', 'run_id', 'lane_id', 'length', 'indexed')

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'run_id', 'start_after', 'status_id', 'requestor')
        read_only_fields = ('date_created', 'date_modified')

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('id', 'request_id', 'analysis_type_id', 'cmd', 'start',
                'stop', 'code', 'pid', 'log')
        read_only_fields = ('date_created', 'date_modified')

class Bcl2fastqSampleAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bcl2fastqSampleAnalysis
        fields = ('id', 'analysis_id', 'sample_id', 'q30', 'cluster')
        read_only_fields = ('date_created', 'date_modified')
