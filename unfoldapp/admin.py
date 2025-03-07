from django.contrib import admin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

from unfoldapp import models
from unfoldapp.models import Report

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

from django.utils.html import format_html

@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'isdeleted', 'createdon', 'modifiedon', 'createdby', 'modifiedby')
    list_display_links = ('id', 'name', 'description')
    list_filter = ('isdeleted', 'createdon', 'modifiedon', 'createdby', 'modifiedby')
    search_fields = ('name', 'description', 'createdon', 'modifiedon', 'createdby', 'modifiedby')
    ordering = ('id',)
    list_per_page = 30

