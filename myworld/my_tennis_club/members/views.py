from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def smjerovi(request):
  template = loader.get_template('smjerovi.html')
  return HttpResponse(template.render())