from django.contrib import admin
#from feincms.admin import tree_editor
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from .models import Provider
from .models import Category

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

#admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Provider)
# admin.site.register(Category)

