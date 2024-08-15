from django.db import models
from django.utils.crypto import get_random_string

class TextSnippet(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('plaintext', 'Plain Text'),
        # Add more languages as needed
    ]

    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    unique_url = models.CharField(max_length=8, unique=True, editable=False)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='plaintext')

    def save(self, *args, **kwargs):
        if not self.unique_url:
            self.unique_url = get_random_string(8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'Untitled Snippet'
