from django.views.generic import ListView, DetailView, CreateView
from reqs.models import Request
from django.contrib.auth.decorators import login_required

@login_required
def new_request():
    pass

class RequestList(ListView):
    model = Request

class RequestDetail(DetailView):
    model = Request

class RequestCreate(CreateView):
    #TODO: Add src from logged-in user and parent from referring link
    model = Request
    fields = ['dest', 'title', 'body']

    @login_required
    def dispatch(self, *args, **kwargs):
        return super(RequestCreate, self).dispatch(*args, **kwargs)

    def get_initial(self):
        #FIXME: This is very likely the wrong way to do this.
        #It may not even work
        initial = super(RequestCreate, self).get_initial(*args, **kwargs)
        initial['src'] = self.request.user.id
        initial['parent'] = self.request.GET.get('parent', default=None)
        return initial
