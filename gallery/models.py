from django.db import models


class GalleryImage(models.Model):
    """Model for storing preschool gallery images."""
    CATEGORY_CHOICES = [
        ('A', 'Activities'),
        ('E', 'Events'),
        ('C', 'Classroom'),
        ('O', 'Other'),
    ]

    title = models.CharField(max_length=200, verbose_name="Image Title")
    image = models.ImageField(upload_to='gallery/', verbose_name="Image File")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='O', verbose_name="Category")
    description = models.TextField(blank=True, verbose_name="Description")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded On")
    is_active = models.BooleanField(default=True, verbose_name="Show in Gallery")

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title
