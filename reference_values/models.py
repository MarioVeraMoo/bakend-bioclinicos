from django.db import models
from tests.models import Tests
from django.db.models import SET_NULL

class referencevalue(models.Model):
    text1 = models.CharField(max_length=255, null=True, blank=True)
    value1 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    character1 = models.CharField(max_length=25, null=True, blank=True)
    value2 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    text2 = models.CharField(max_length=255, null=True, blank=True)
    value3 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    character2 = models.CharField(max_length=25, null=True, blank=True)
    value4 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    text3 = models.CharField(max_length=255, null=True, blank=True)
    value5 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    character5 = models.CharField(max_length=25, null=True, blank=True)
    value6 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    test = models.ForeignKey(Tests, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.text1