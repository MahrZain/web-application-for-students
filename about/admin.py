from django.contrib import admin
from .models import *
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'url')
admin.site.register(About, AboutAdmin)
