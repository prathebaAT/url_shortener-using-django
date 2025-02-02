

from django.db import models

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"

