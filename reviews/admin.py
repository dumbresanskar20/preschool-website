from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['parent_name', 'child_name', 'rating', 'created_at', 'is_approved']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['parent_name', 'child_name', 'review_message']
    readonly_fields = ['created_at']
    list_editable = ['is_approved']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'

    actions = ['approve_reviews', 'disapprove_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} review(s) approved.")
    approve_reviews.short_description = "✅ Approve selected reviews"

    def disapprove_reviews(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"{queryset.count()} review(s) disapproved.")
    disapprove_reviews.short_description = "❌ Disapprove selected reviews"
