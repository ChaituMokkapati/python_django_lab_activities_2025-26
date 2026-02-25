from django.db import models

class Slide(models.Model):
    title = models.CharField(max_length=120)
    caption = models.TextField(blank=True)
    image_url = models.URLField(
        max_length=500,
        help_text="Paste a direct image URL (e.g., from picsum.photos)"
    )
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title
