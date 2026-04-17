from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_preview', 'uploaded_at', 'is_active']
    list_filter = ['category', 'is_active', 'uploaded_at']
    search_fields = ['title', 'description']
    readonly_fields = ['uploaded_at', 'image_preview_large']
    list_editable = ['is_active', 'category']
    ordering = ['-uploaded_at']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 5px; object-fit: cover;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"
    
    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 300px; max-width: 100%; border-radius: 8px;" />', obj.image.url)
        return "No Image"
    image_preview_large.short_description = "Current Image Preview"
