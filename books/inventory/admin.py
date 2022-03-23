from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import *

# Register your models here.


class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
    model = Category
    list_display = ("tree_actions", "indented_title")
    list_display_links = ("indented_title",)


admin.site.register(Category, MyDraggableMPTTAdmin)
admin.site.register(ProductInventory)
