from django.http import HttpResponse
from django.template import loader
from django.views import View
from .models import Article

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def smjerovi(request, slug):
  articles = Article.objects.all()
  template = loader.get_template('smjerovi.html',)
  context = {'articles': articles}
  return HttpResponse(template.render(context, request))