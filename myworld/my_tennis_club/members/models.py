from django.db import models


class Article(models.Model):
  title = models.CharField(max_length=64)
  published = models.DateField(null=True)
  body = models.TextField()
  image = models.ImageField(upload_to='img/')
  slug = models.SlugField(default="", null=False)

  def __str__(self):
    return f"{self.title}"
