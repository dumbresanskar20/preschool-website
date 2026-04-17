from django.db import models


class ContactMessage(models.Model):
    """Model for contact form messages."""
    name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number", blank=True)
    subject = models.CharField(max_length=300, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Received On")
    is_read = models.BooleanField(default=False, verbose_name="Read by Admin")
    is_replied = models.BooleanField(default=False, verbose_name="Replied")

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%d %b %Y')})"
