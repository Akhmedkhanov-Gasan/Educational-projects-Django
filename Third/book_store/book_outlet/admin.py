from django.contrib import admin
from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'rating', 'author', 'is_bestselling')
    search_fields = ['title']
    list_filter = ['rating', 'author']
    ordering = ('rating',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)
