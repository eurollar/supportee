from comments.models import Comment
from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'ticket', 'published')
    list_filter = ('author', 'published')


admin.site.register(Comment, CommentAdmin)
