from modeltranslation.translator import register,TranslationOptions
from . import models

@register(models.News)
class NewsTranslation(TranslationOptions):
    fields = ['title','description','content']

@register(models.Category)
class CategoryTranslation(TranslationOptions):
    fields = ['name']