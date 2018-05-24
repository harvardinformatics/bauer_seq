from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
        url(r'^request/new/$', RequestCreateForm.as_view(), name='request_create'),
        url(r'^request/edit/(?P<pk>\d+)/$', RequestEditForm.as_view(), name='request_edit'),
        url(r'^request/(?P<pk>\d+)/$', RequestDetail.as_view(), name='request_detail'),
        url(r'^requests/$', RequestList.as_view(), name='request_list'),

        # below are all the API endpoints
        url(r'^api/instruments/$', InstrumentCreate.as_view(), name='api_instrument_create'),
        url(r'^api/sample_types/$', SampleTypeCreate.as_view(), name='api_sample_type_create'),
        url(r'^api/runs/$', RunCreate.as_view(), name='api_run_create'),
        url(r'^api/runs/(?P<pk>[0-9]+)/$', RunMod.as_view(), name='api_run_modify'),
        url(r'^api/lanes/$', LaneCreate.as_view(), name='api_lane_create'),
        url(r'^api/lanes/(?P<pk>[0-9]+)/$', LaneMod.as_view(), name='api_lane_modify'),
        url(r'^api/samples/$', SampleCreate.as_view(), name='api_sample_create'),
        url(r'^api/samples/(?P<pk>[0-9]+)/$', SampleMod.as_view(), name='api_sample_modify'),
        url(r'^api/reads/$', ReadCreate.as_view(), name='api_read_create'),
        url(r'^api/reads/(?P<pk>[0-9]+)/$', ReadMod.as_view(), name='api_read_modify'),
        url(r'^api/requests/$', RequestCreate.as_view(), name='api_request_create'),
        url(r'^api/requests/(?P<pk>[0-9]+)/$', RequestMod.as_view(), name='api_request_modify'),
        url(r'^api/analyses/$', AnalysisCreate.as_view(), name='api_analysis_create'),
        url(r'^api/analyses/(?P<pk>[0-9]+)/$', AnalysisMod.as_view(), name='api_analysis_modify'),
        url(r'^api/bcl2fastq_sample_analyses/$', Bcl2fastqSampleAnalysisCreate.as_view(), name='api_bcl2fastq_sample_analysis_create'),
        url(r'^api/bcl2fastq_sample_analyses/(?P<pk>[0-9]+)/$', Bcl2fastqSampleAnalysisMod.as_view(), name='api_bcl2fastq_sample_analysis_modify')
}

urlpatterns = format_suffix_patterns(urlpatterns)
