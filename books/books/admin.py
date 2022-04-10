from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter
from .models import *

# Register your models here.
# class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
#     model = Category
#     list_display = ('tree_actions', 'indented_title')
#     list_display_links = ('indented_title',)

# class ReviewInLine(admin.TabularInline):
#     model = Review

# class BookAdmin(admin.ModelAdmin):
#     model = Book
#     inlines = [
#         ReviewInLine,
#     ]
#     list_display = ('title', 'author', 'price',)
#     list_filter = (
#         ('category', TreeRelatedFieldListFilter),
#     )


# admin.site.register(Book, BookAdmin)
# admin.site.register(Category, MyDraggableMPTTAdmin)
