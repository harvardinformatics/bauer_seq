from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
        # below are all the API endpoints
        url(r'^instruments/$', InstrumentCreate.as_view(), name='api_instrument_create'),
        url(r'^runs/$', RunCreate.as_view(), name='api_run_create'),
        url(r'^run_list/$', RunList.as_view(), name='api_run_list'),
        url(r'^runs/(?P<name>[a-zA-Z0-9_]+)/$', RunMod.as_view(), name='api_run_modify'),
        url(r'^lanes/$', LaneCreate.as_view(), name='api_lane_create'),
        url(r'^lanes/(?P<pk>[0-9]+)/$', LaneMod.as_view(), name='api_lane_modify'),
        url(r'^samples/$', SampleCreate.as_view(), name='api_sample_create'),
        url(r'^samples/(?P<pk>[0-9]+)/$', SampleMod.as_view(), name='api_sample_modify'),
        url(r'^reads/$', ReadCreate.as_view(), name='api_read_create'),
        url(r'^reads/(?P<pk>[0-9]+)/$', ReadMod.as_view(), name='api_read_modify'),
        url(r'^requests/$', RequestCreate.as_view(), name='api_request_create'),
        url(r'^requests/(?P<pk>[0-9]+)/$', RequestMod.as_view(), name='api_request_modify'),
        url(r'^analyses/$', AnalysisCreate.as_view(), name='api_analysis_create'),
        url(r'^analyses/(?P<pk>[0-9]+)/$', AnalysisMod.as_view(), name='api_analysis_modify'),
        url(r'^bcl2fastq_sample_analyses/$', Bcl2fastqSampleAnalysisCreate.as_view(), name='api_bcl2fastq_sample_analysis_create'),
        url(r'^bcl2fastq_sample_analyses/(?P<pk>[0-9]+)/$', Bcl2fastqSampleAnalysisMod.as_view(), name='api_bcl2fastq_sample_analysis_modify')
}

urlpatterns = format_suffix_patterns(urlpatterns)
