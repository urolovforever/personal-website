from django.contrib import admin
from .models import Profile, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for Profile model.
    """
    list_display = ['name', 'email', 'phone', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Media', {
            'fields': ('github_url', 'linkedin_url', 'telegram_url')
        }),
        ('Files', {
            'fields': ('cv_file',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        """
        Only allow adding if no profile exists yet
        """
        if Profile.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        """
        Prevent deletion of profile
        """
        return False


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
