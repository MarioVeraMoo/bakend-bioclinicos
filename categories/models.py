from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField(null=True, blank=True)
    miniature = models.ImageField(upload_to='categories/images/', null=True, blank=True)

    def __str__(self):
        return self.category