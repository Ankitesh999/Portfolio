from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'order', 'is_featured', 'created_at', 'updated_at']
    list_filter = ['is_featured', 'created_at', 'technologies']
    search_fields = ['title', 'description', 'content']
    list_editable = ['order', 'is_featured']
    ordering = ['order', '-created_at']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'content')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'live_url', 'github_url')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Display Options', {
            'fields': ('order', 'is_featured')
        }),
    )
