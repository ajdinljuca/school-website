from django.http import HttpResponse
from django.template import loader
from django.views import View
from .models import Article

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def kontakt(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def upis(request):
  template = loader.get_template('upis.html')
  return HttpResponse(template.render())

def prostor(request):
  template = loader.get_template('prostor.html')
  return HttpResponse(template.render())

def smjerovi(request, slug):
  articles = Article.objects.all()
  template = loader.get_template('smjerovi.html',)
  context = {'articles': articles}
  return HttpResponse(template.render(context, request))

def vijesti(request, slug):
  articles = Article.objects.all()
  template = loader.get_template('news2.html',)
  context = {'articles': articles}
  return HttpResponse(template.render(context, request))
  #"Articles" context part was unchanged after copy paste of earlier view

def događaji(request, slug):
  articles = Article.objects.all()
  template = loader.get_template('news.html',)
  context = {'articles': articles}
  #The html for events tab is missing so news html was implemented instead
