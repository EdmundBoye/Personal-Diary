
from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_private = models.BooleanField(default=True)
    tags = models.CharField(max_length=250, blank=True, help_text='Comma-separated tags')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]
