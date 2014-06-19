from django.conf.urls import patterns, include, url

from reqs.views import RequestList, RequestDetail, RequestCreate

urlpatterns = patterns('',
    url(r'(?P<pk>[0-9]+)/?$', RequestDetail.as_view(), name='request-detail'),
    url(r'new/?$', RequestCreate.as_view(), name='request-create'),
    url(r'', RequestList.as_view(), name='request-list'),
)
