from django.contrib import admin
#from feincms.admin import tree_editor
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from .models import *

admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

class SupplierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description', 'slug', 'type', 'price_range']}),
        ('Infos générales', {'fields': ['image', 'category', ('adress', 'postal_code', 'city', 'country')]}),
        ('Réception', {'fields': [('caterer_free', 'brewer_free', 'gite_included', 'furnitures_included'), ('minhosts', 'maxhosts')]}),
        ('Traiteur', {'fields': [('buffet', 'echoppes', 'menu', 'dishes_included')]}),
        ('Tags', {'fields':['tag']})
    ]
    filter_horizontal = ['tag']
    ##inlines = [TagInline]

#admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Tag)

