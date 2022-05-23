from django.contrib import admin

from comments.models import Comment
from tickets.models import Ticket


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class TicketAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'author', 'status', 'create')
    fields = ['title', 'text', ('author', 'status')]
    list_filter = ('status', 'author', 'create')


admin.site.register(Ticket, TicketAdmin)
