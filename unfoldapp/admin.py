from django.contrib import admin,messages
from unfold.contrib.forms.widgets import WysiwygWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.db.models import TextChoices
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from unfoldapp import models
from unfold.decorators import display 
from django.utils.translation import gettext_lazy as _
from unfoldapp.models import PublishedStatus
from django.contrib.admin.models import LogEntry
from django.utils import timezone
from modeltranslation.admin import TabbedTranslationAdmin
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

@admin.register(models.News,)
class NewsAdmin(ModelAdmin,TabbedTranslationAdmin):
    list_display = ['image_tag','title','short_description','short_content','category','show_views','show_is_published','created_at','updated_at']
    list_display_links = ['image_tag','title','short_description','short_content','category','show_views','show_is_published','created_at','updated_at']
    exclude = ["updated_at"]
    search_fields = ['title','description','category__name','content']
    list_filter = ['is_published']
    actions = ['publish_news','hide_news']
    exclude = ['views','updated_at']
    date_hierarchy = 'created_at'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('views',)
        return super().get_readonly_fields(request, obj)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Изображение'

    def short_content(self,obj):
        return obj.content[:10]+'...'
    short_content.short_description = 'Контент'

    def short_description(self,obj):
        return obj.description[:10]+'...'
    short_description.short_description = 'Описание'

    def is_published_display(self,obj):
        return obj.get_is_published_display()
    
    is_published_display.short_description = 'Опубликовано'

    @display(description='Опубликовано',
             ordering='is_published',
             label={
                 PublishedStatus.YES :'success',
                 PublishedStatus.NO: 'danger'
             },)
    def show_is_published(self,obj):
        return (obj.is_published, obj.get_is_published_display())

    @display(description='Просмотры',
             ordering='views',
             label={
                 'views': None,
             })
    def show_views(self,obj):
        return ('views', str(obj.views))   # преобразуем в строку

    @admin.action(description='Опубликовать новость')
    def publish_news(self, request, queryset):
        filtered = queryset.exclude(is_published=True).update(is_published=True,updated_at =timezone.now())
        return self.message_user(request, f'Опубликовано : {filtered}',level=messages.SUCCESS)

    @admin.action(description='Скрыть новость')
    def hide_news(self, request, queryset):
        filtered = queryset.exclude(is_published=False).update(is_published=False,updated_at = timezone.now())
        return self.message_user(request, f'Скрыто : {filtered}',level=messages.ERROR)

@admin.register(models.Category)
class CategoryAdmin(ModelAdmin,TabbedTranslationAdmin):
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


    
@admin.register(LogEntry)
class LogEntryAdmin(ModelAdmin):
    list_display = ['user','object_repr','content_type','action_flag','action_time']
    list_display_links = None

    def has_add_permission(self, request):
        return False
    
    def has_add_permission(self, request):
            return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
