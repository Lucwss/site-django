from django.contrib import admin
from .models import Post
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status', 'created_at', 'updated_at')
    list_filter = ('status','title')
    search_fields = ["title", "content", "created_at"]
    prepopulated_fields = {'slug': ('title', 'content')}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'likes', 'shares', 'created_at', 'updated_at')
    list_filter = ('content','likes', 'shares')
    search_fields = ["content", "created_at", "likes", "shares"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)