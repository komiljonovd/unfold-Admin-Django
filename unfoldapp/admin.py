from django.contrib import admin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from django.utils.html import format_html

from unfoldapp import models

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

@admin.register(models.News)
class NewsAdmin(ModelAdmin):
    list_display = ['image_tag','title','short_description','short_content','category','is_published','created_at','updated_at']
    list_display_links = ['image_tag','title','short_description','short_content','category','is_published','created_at','updated_at']
    exclude = ["updated_at"]
    search_fields = ['title','description','category__name','content']
    list_filter = ['is_published']

    date_hierarchy = 'created_at'

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Изображение'

    def short_content(self,obj):
        return obj.content[:100]+'...'
    short_content.short_description = 'Контент'

    def short_description(self,obj):
        return obj.description[:100]+'...'
    short_description.short_description = 'Описание'


@admin.register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['image_tag','name','created_at','updated_at']
    list_display_links = ['image_tag','name','created_at','updated_at']
    exclude = ["updated_at"]
    search_fields = ['name']
    date_hierarchy = 'created_at'

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Изображение'


    
    
