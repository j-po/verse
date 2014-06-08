from django.conf.urls import patterns, include, url

from reqs.views import RequestList, RequestDetail

urlpatterns = patterns('',
    url(r'^reqs/?$', RequestList.as_view()),
    url(r'^reqs/(?P<request_id>[0-9]*)/?', RequestDetail.as_view()),
)
