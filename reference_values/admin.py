from django.contrib import admin
from reference_values.models import referencevalue
# Register your models here.
@admin.register(referencevalue)
class ExamsAdmin(admin.ModelAdmin):
    list_display = ['test']