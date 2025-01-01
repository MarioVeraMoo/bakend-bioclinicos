from django.contrib import admin
from tests.models import Tests
# Register your models here.
@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ['test']
