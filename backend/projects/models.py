from django.db import models


class Project(models.Model):
    """
    Model representing a portfolio project.
    """
    title = models.CharField(max_length=200, help_text="Project title")
    description = models.TextField(help_text="Detailed project description")
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Project screenshot or thumbnail"
    )
    github_link = models.URLField(
        blank=True,
        null=True,
        help_text="GitHub repository URL"
    )
    live_link = models.URLField(
        blank=True,
        null=True,
        help_text="Live demo URL"
    )
    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text="Technologies used (comma-separated)"
    )
    project_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Type of project (e.g., Web App, Mobile App, API)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
