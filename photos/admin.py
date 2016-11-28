from django.contrib import admin
from .models import Post
from .models import Comment
from .models import Category
from .models import Tag
from profiles.models import Profile


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'created_at', )
    list_display_links = ('id', 'created_at', )
    ordering = ('-id', '-created_at', )
    inlines = (CommentInlineAdmin, )
    search_fields = ('id', 'content', )
    list_filter = ('category', 'tags', )
    date_hierarchy = 'created_at'


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('id', 'name',)
    ordering = ('id', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Profile,ProfileAdmin)
