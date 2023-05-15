from django.http import HttpResponse
from django.template import loader
from django.views import View
from .models import Article
from .models import Vijesti
# Untested imports:
from django.shortcuts import get_object_or_404, render
from .models import Struka, Smijer

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

def događaji(request):
  template = loader.get_template('događaji.html')
  return HttpResponse(template.render())

def sekcije(request):
  template = loader.get_template('sekcije.html')
  return HttpResponse(template.render())

"""
def smijer(request, slug):
  articles = Article.objects.all()
  template = loader.get_template('smijer.html',)
  context = {'articles': articles}
  return HttpResponse(template.render(context, request))
"""

def struke(request):
  template = loader.get_template('struke.html')
  return HttpResponse(template.render())


# This might produce some unwanted bugs:

def struka_smijer_view(request, struka_slug, smijer_slug):
    struka = get_object_or_404(Struka, slug=struka_slug)
    smjerovi = Smijer.objects.filter(struka=struka)
    
    # Render the template with the selected branch and profession
    return render(request, 'your_template.html', {
        'struka': struka,
        'smjerovi': smjerovi,
        'izabrani_smijer': get_object_or_404(smjerovi, slug=smijer_slug) if smijer_slug else None
    })


def vijesti(request):
  najnovija_vijest = Vijesti.objects.latest('objavljen')
  nove_vijesti = Vijesti.objects.order_by('-objavljen')[1:7]
  stare_vijesti = Vijesti.objects.order_by('-objavljen')[7:]
  #Worked right : vijesti = Vijesti.objects.all().order_by('-id')
  template = loader.get_template('vijesti.html')
  context = {
   #Worked right : 'vijesti': vijesti,

  'najnovija_vijest': najnovija_vijest,
  'nove_vijesti': nove_vijesti,
  'stare_vijesti': stare_vijesti,
 
  }
  return HttpResponse(template.render(context, request))


def clanak(request, id):
  clanak = Vijesti.objects.get(id=id)
  template = loader.get_template('clanak.html')
  context = {
    'clanak': clanak,
  }
  return HttpResponse(template.render(context, request))        