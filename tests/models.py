from django.db import models
from subexams.models import SubExam
from django.db.models import SET_NULL


class Tests(models.Model):
    test = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    unitofmeasurement = models.CharField(max_length=255, null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    subexam = models.ForeignKey(SubExam, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.test