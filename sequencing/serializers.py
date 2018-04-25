from rest_framework import serializers
from .models import Run, Instrument

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'type')

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('id', 'name', 'flowcell', 'lot', 'expiration', 'instrument_id')
        read_only_fields = ('date_created', 'date_modified')


