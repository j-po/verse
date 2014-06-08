from django.views.generic import ListView, DetailView
from reqs.models import Request

class RequestList(ListView):
    model = Request

class RequestDetail(DetailView):
    model = Request
