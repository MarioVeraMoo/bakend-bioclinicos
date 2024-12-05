from django.db import models
from categories.models import Category
from django.db.models import SET_NULL


class Exam(models.Model):
    exam = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    titleExam = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    indications = models.TextField(null=True, blank=True)
    miniature = models.ImageField(upload_to='categories/images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.exam
