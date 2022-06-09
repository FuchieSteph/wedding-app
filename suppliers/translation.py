from modeltranslation.translator import translator, TranslationOptions
from .models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ('description', 'name')

class TagTranslationOptions(TranslationOptions):
    fields = ( 'name',)

translator.register(Category, CategoryTranslationOptions)
translator.register(Tag, TagTranslationOptions)