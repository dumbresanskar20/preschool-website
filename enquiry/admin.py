from django.contrib import admin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'child_name', 'child_age', 'phone', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['parent_name', 'child_name', 'email', 'phone']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Parent Information', {
            'fields': ('parent_name', 'email', 'phone')
        }),
        ('Child Information', {
            'fields': ('child_name', 'child_age')
        }),
        ('Enquiry Details', {
            'fields': ('message', 'created_at', 'is_read')
        }),
    )
