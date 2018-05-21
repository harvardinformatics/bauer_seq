from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = {
        url(r'^create_request/$', RequestCreateForm.as_view(), name='create request'),
        url(r'^edit_request/(?P<pk>\d+)/$', RequestEditForm.as_view(), name='request edit'),
        url(r'^request_detail/(?P<pk>\d+)/$', RequestDetail.as_view(), name='request detail'),
        url(r'^request_list/$', RequestList.as_view(), name='request list'),

        # below are all the API endpoints
        url(r'^instruments/$', InstrumentCreate.as_view(), name='instrument create'),
        url(r'^sample_types/$', SampleTypeCreate.as_view(), name='sample type create'),
        url(r'^runs/$', RunCreate.as_view(), name='run create'),
        url(r'^runs/(?P<pk>[0-9]+)/$', RunMod.as_view(), name='run modify'),
        url(r'^lanes/$', LaneCreate.as_view(), name='lane create'),
        url(r'^lanes/(?P<pk>[0-9]+)/$', LaneMod.as_view(), name='lane modify'),
        url(r'^samples/$', SampleCreate.as_view(), name='sample create'),
        url(r'^samples/(?P<pk>[0-9]+)/$', SampleMod.as_view(), name='sample modify'),
        url(r'^reads/$', ReadCreate.as_view(), name='read create'),
        url(r'^reads/(?P<pk>[0-9]+)/$', ReadMod.as_view(), name='read modify'),
        url(r'^requests/$', RequestCreate.as_view(), name='request create'),
        url(r'^requests/(?P<pk>[0-9]+)/$', RequestMod.as_view(), name='request modify'),
        url(r'^analyses/$', AnalysisCreate.as_view(), name='analysis create'),
        url(r'^analyses/(?P<pk>[0-9]+)/$', AnalysisMod.as_view(), name='analysis modify'),
        url(r'^bcl2fastq_sample_analyses/$', Bcl2fastqSampleAnalysisCreate.as_view(), name='bcl2fastq sample analysis create'),
        url(r'^bcl2fastq_sample_analyses/(?P<pk>[0-9]+)/$', Bcl2fastqSampleAnalysisMod.as_view(), name='bcl2fastq sample analysis modify')
}

urlpatterns = format_suffix_patterns(urlpatterns)
