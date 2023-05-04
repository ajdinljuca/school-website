from django.db import models
# New import (not tested)
from django.utils.text import slugify


class Article(models.Model):
  title = models.CharField(max_length=64)
  published = models.DateField(null=True)
  body = models.TextField()
  image = models.ImageField(upload_to='img/')
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return f"{self.title}"
  
  

# This might produce some unwanted bugs:
# The following code defines models for professions tab so the urls can 
# generate properly


class Struka(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(unique=True, editable=False)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name

class Smijer(models.Model):
  name = models.CharField(max_length=50)
  slug = models.SlugField(unique=True, editable=False)
  struka = models.ForeignKey(Struka, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super().save(*args, **kwargs)

    def __str__(self):
      return self.name

class Vijesti(models.Model):
  name = models.CharField(max_length=255)
  test = models.CharField(max_length=255)