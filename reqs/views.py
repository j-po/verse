from django.views.generic import ListView, DetailView, CreateView
from reqs.models import VerseRequest

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class RequestList(ListView):
    model = VerseRequest
    template_name = 'reqs/request_list.html'

class RequestDetail(DetailView):
    model = VerseRequest
    template_name = 'reqs/request_detail.html'

class RequestCreate(CreateView):
    #TODO: Add src from logged-in user and parent from referring link
    model = VerseRequest
    fields = ['dest', 'title', 'body']
    template_name = 'reqs/request_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RequestCreate, self).dispatch(*args, **kwargs)

    def get_initial():
        #FIXME: This is very likely the wrong way to do this.
        #It may not even work
        initial = super(RequestCreate, self).get_initial(*args, **kwargs)
        initial['src'] = self.request.user.id
        initial['parent'] = self.request.GET.get('parent', default=None)
        return initial
