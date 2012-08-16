# Create your views here.
from django.template import Context, loader, RequestContext
from django.http import HttpResponse


def index(request):
    t = loader.get_template('index/index.html')
    c = RequestContext(request)
    # c = Context.({
    #    'response' : 'index_action',
    #})
    return HttpResponse (t.render(c))





