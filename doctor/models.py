from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    midle_name = models.CharField(max_length=50)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(max_length=254)

def __str__(self):
    return self.first_name