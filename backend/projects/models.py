from django.db import models


class Profile(models.Model):
    """
    Model representing personal profile information.
    Should only have one instance.
    """
    name = models.CharField(max_length=200, default="Nizomjon Urolov", help_text="Your full name")
    title = models.CharField(
        max_length=200,
        default="Junior Web Developer | Cybersecurity Enthusiast",
        help_text="Your professional title"
    )
    bio = models.TextField(
        help_text="Short biography",
        default="Passionate about building clean, responsive, and user-friendly websites. Currently strengthening cybersecurity skills to create secure and efficient web applications."
    )
    profile_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True,
        help_text="Your profile photo"
    )
    email = models.EmailField(default="nizomjonurolov24@gmail.com")
    phone = models.CharField(max_length=50, blank=True, default="+998 95-039-36-69")
    location = models.CharField(max_length=200, blank=True, default="Pilla street, 78, Tashkent")
    github_url = models.URLField(blank=True, default="https://github.com/urolovforever")
    linkedin_url = models.URLField(blank=True, default="https://www.linkedin.com/in/nizomjonurolov")
    telegram_url = models.URLField(blank=True, default="https://t.me/urolovnizomjon")
    cv_file = models.FileField(
        upload_to='cv/',
        blank=True,
        null=True,
        help_text="Upload your CV/Resume PDF"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Override save to ensure only one profile exists
        """
        if not self.pk and Profile.objects.exists():
            # If trying to create a new instance and one already exists
            raise ValueError('Only one Profile instance is allowed')
        return super().save(*args, **kwargs)


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
