from django.contrib import admin
from subexams.models import SubExam
# Register your models here.
@admin.register(SubExam)
class ExamsAdmin(admin.ModelAdmin):
    list_display = ['subexam']
