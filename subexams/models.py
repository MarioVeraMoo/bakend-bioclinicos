from django.db import models
from exams.models import Exam
from django.db.models import SET_NULL


class SubExam(models.Model):
    subexam = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    exam = models.ForeignKey(Exam, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.subexam