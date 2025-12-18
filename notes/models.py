from django.db import models
from django.urls import reverse

# Create your models here.

class Note(models.Model):
    """Model for a single sticky note."""
    title = models.CharField(max_length=120, help_text="Short title for the note")
    content = models.TextField(help_text="Content of the sticky note")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        """Return the canonical URL to view this note's detail page."""
        return reverse('notes:note_detail', kwargs={'pk': self.pk})