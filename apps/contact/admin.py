from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'timestamp', 'is_read']
    list_filter = ['is_read', 'timestamp']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['-timestamp']
    readonly_fields = ['name', 'email', 'subject', 'message', 'timestamp']
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"
