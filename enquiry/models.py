from django.db import models


class Enquiry(models.Model):
    """Model for parent enquiries about admission."""
    parent_name = models.CharField(max_length=200, verbose_name="Parent Name")
    child_name = models.CharField(max_length=200, verbose_name="Child Name")
    child_age = models.PositiveIntegerField(verbose_name="Child Age (Years)")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Message / Query", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted On")
    is_read = models.BooleanField(default=False, verbose_name="Read by Admin")

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.parent_name} - {self.child_name} ({self.created_at.strftime('%d %b %Y')})"
