from django.contrib import admin

from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'ticket', 'published')
    list_filter = ('author', 'published')


admin.site.register(Comment, CommentAdmin)
