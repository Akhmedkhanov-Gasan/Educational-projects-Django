from django.contrib import admin
from .models import Tag, Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'excerpt', 'date')
    search_fields = ('title',)
    list_filter = ('author', 'date', 'tags')
    prepopulated_fields = {'slug': ('title',)}




admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
