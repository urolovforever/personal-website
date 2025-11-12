from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin configuration for Project model.
    """
    list_display = [
        'title',
        'project_type',
        'created_at',
        'has_github_link',
        'has_live_link'
    ]
    list_filter = ['project_type', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Links', {
            'fields': ('github_link', 'live_link')
        }),
        ('Additional Details', {
            'fields': ('technologies', 'project_type')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_github_link(self, obj):
        """Display if project has GitHub link."""
        return bool(obj.github_link)
    has_github_link.boolean = True
    has_github_link.short_description = 'GitHub'

    def has_live_link(self, obj):
        """Display if project has live demo link."""
        return bool(obj.live_link)
    has_live_link.boolean = True
    has_live_link.short_description = 'Live Demo'
