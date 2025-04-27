from django.contrib import admin
from blogapp.models import Category, Post, Comment, Author, Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('categories',)
    ordering = ('-created_at',)
    fields = ('title', 'content', 'categories')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    search_fields = ('author',)
    list_filter = ('created_at',)
    raw_id_fields = ('post',)
    fields = ('post', 'author', 'content')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)
    raw_id_fields = ('posts',)
    fields = ('name', 'email', 'bio', 'posts')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    raw_id_fields = ('posts',)
    fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
