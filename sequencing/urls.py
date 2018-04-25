from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RunCreate, RunMod

urlpatterns = {
        url(r'^runs/$', RunCreate.as_view(), name='run create'),
        url(r'^runs/(?P<pk>[0-9]+)/$', RunMod.as_view(), name='run modify')
}

urlpatterns = format_suffix_patterns(urlpatterns)
