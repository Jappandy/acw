from django.views.generic import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(TemplateView):
    template_name = "index.html"

class HomeView(TemplateView):
    template_name = "home.html"
    
    
class BulmaView(TemplateView):
    template_name = "bulma.html"    