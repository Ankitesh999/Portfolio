from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of title")
    description = models.TextField(help_text="Brief description for project cards")
    content = models.TextField(help_text="Full project details")
    technologies = models.CharField(max_length=500, help_text="Comma-separated technologies")
    live_url = models.URLField(blank=True, null=True, help_text="Live project URL")
    github_url = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    featured_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})

    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
