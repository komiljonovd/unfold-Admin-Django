from django.contrib import admin
from unfold.contrib.forms.widgets import WysiwygWidget

from unfoldapp.models import Report
from unfold.admin import ModelAdmin
from django.db import models


# Register your models here.

@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'isdeleted', 'createdon', 'modifiedon', 'createdby', 'modifiedby')
    list_display_links = ('id', 'name', 'description')
    list_filter = ('isdeleted', 'createdon', 'modifiedon', 'createdby', 'modifiedby')
    search_fields = ('name', 'description', 'isdeleted', 'createdon', 'modifiedon', 'createdby', 'modifiedby')
    ordering = ('id',)
    list_per_page = 30

