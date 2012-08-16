# Create your views here.
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from pyactiveresource.activeresource import ActiveResource

class Project(ActiveResource):
	_site = 'http://54.245.23.219:8080/'
	_user = 'admin'
	_password = 'admin'

def index(request):
	projects = Project.find()
	projectslist = projects.attributes
	t = loader.get_template('index/index.html')
    c = RequestContext(request)
    # c = Context.({
    #    'response' : 'index_action',
    #})
    return HttpResponse (t.render(c))





