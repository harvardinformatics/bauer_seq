from django.db import models
from django.urls import reverse
from djvocab import getChoices

# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100,
            choices = (('nextseq', 'nextseq'), ('hiseq', 'hiseq')),
            default = 'nextseq')

class Run(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    flowcell = models.CharField(max_length=100, blank = True, null = True)
    lot = models.CharField(max_length=100, blank = True, null = True)
    expiration = models.DateField(blank = True, null = True)
    instrument = models.ForeignKey('Instrument', on_delete = models.PROTECT)

    def get_absolute_url(self):
        return reverse('run_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Lane(models.Model):
    number = models.IntegerField()
    run = models.ForeignKey('Run', on_delete = models.CASCADE, related_name = 'run_lanes')

    def __str__(self):
        return str(self.number)

class Sample(models.Model):
    name = models.CharField(max_length=100)
    run = models.ForeignKey('Run', on_delete = models.PROTECT, related_name = 'run_samples')
    lane = models.ForeignKey('Lane', on_delete = models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    description = models.CharField(max_length=100)
    index1 = models.CharField(max_length=100, blank = True, null = True)
    index2 = models.CharField(max_length=100, blank = True, null = True)
    sample_type = models.CharField(max_length=100, choices=((v.value, v.value) for v in getChoices('sample.sample_type')), blank = True, null = True)

    def get_absolute_url(self):
        return reverse('sample_detail', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse('sample_edit', kwargs={'pk': self.pk})

class Read(models.Model):
    number = models.IntegerField()
    run = models.ForeignKey('Run', on_delete = models.CASCADE)
    length = models.IntegerField(blank = True, null = True)
    indexed = models.BooleanField(default = False)

class Status(models.Model):
    name = models.CharField(max_length=100,
            choices = (('pending', 'pending'),
        ('processing', 'processing'), ('complete', 'complete'), ('failed',
            'failed')),
            default = 'pending')

class Request(models.Model):
    run = models.ForeignKey('Run', on_delete = models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    start_after = models.DateTimeField(auto_now = True)
    status = models.ForeignKey('Status', on_delete = models.PROTECT)
    step = models.CharField(max_length = 100, choices = (('demultiplex', 'demultiplex'),
        ('quality', 'quality'), ('count', 'count'), ('publish',
            'publish')), blank = True, null = True)
    requestor = models.CharField(max_length=100, blank = True, null = True)

    def get_absolute_url(self):
        return reverse('request_detail', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse('request_edit', kwargs={'pk': self.pk})

class AnalysisType(models.Model):
    name = models.CharField(max_length=100,
            choices = (('bcl2fastq', 'bcl2fastq'), ('fastqc', 'fastqc')),
            default = 'bcl2fastq')
    class Meta:
        db_table = 'analysis_type'

class Analysis(models.Model):
    request = models.ForeignKey('Request', on_delete = models.PROTECT)
    analysis_type = models.ForeignKey('AnalysisType', on_delete =
            models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    cmd = models.CharField(max_length=255)
    start = models.DateTimeField(null = True)
    stop = models.DateTimeField(null = True)
    code = models.IntegerField(null = True)
    pid = models.IntegerField(null = True)
    log = models.CharField(max_length=255, null = True)

class Bcl2fastqSampleAnalysis(models.Model):
    analysis = models.ForeignKey('Analysis', on_delete = models.PROTECT)
    sample = models.ForeignKey('Sample', on_delete = models.PROTECT)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    q30 = models.FloatField()
    cluster = models.IntegerField()
    class Meta:
        db_table = 'sequencing_bcl2fastq_sample_analysis'
