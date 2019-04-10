from django.contrib import admin
from shop.models import Category, Book



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'price', 'stock', 'available', 'created', 'update']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['available', 'created', 'update', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
