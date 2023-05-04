from django.contrib import admin
from .models import Article
from .models import Struka
from .models import Smijer
from .models import Vijesti

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
  list_display = ("title", "published",)
  prepopulated_fields = {"slug": ("title",)}
  
admin.site.register(Article, ArticleAdmin)


class StrukaAdmin(admin.ModelAdmin):
  list_display = ("name","slug")
  prepopulated_fields = {"slug": ("name",)}
  
admin.site.register(Struka, StrukaAdmin)

class SmijerAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug', 'struka')
  prepopulated_fields = {"slug": ("name",)}
  list_filter = ('struka',)
  
admin.site.register(Smijer, SmijerAdmin)

class VijestiAdmin(admin.ModelAdmin):
  list_display = ("name", "test",)
  
admin.site.register(Vijesti, VijestiAdmin)