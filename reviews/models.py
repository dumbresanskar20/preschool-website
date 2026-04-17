from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    """Model for parent reviews and testimonials."""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    parent_name = models.CharField(max_length=200, verbose_name="Parent Name")
    child_name = models.CharField(max_length=200, verbose_name="Child Name")
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Rating (1-5)"
    )
    review_message = models.TextField(verbose_name="Review Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Review Date")
    is_approved = models.BooleanField(default=False, verbose_name="Approved by Admin")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.parent_name} - {self.rating}★ ({self.child_name})"

    @property
    def star_range(self):
        """Returns range for star rendering in templates."""
        return range(1, self.rating + 1)

    @property
    def empty_star_range(self):
        """Returns range for empty stars."""
        return range(self.rating + 1, 6)
