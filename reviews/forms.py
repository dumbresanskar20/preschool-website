from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['parent_name', 'child_name', 'rating', 'review_message']
        widgets = {
            'parent_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Your Full Name",
            }),
            'child_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Your Child's Name",
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control',
            }),
            'review_message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your experience with Rainbow Preschool...',
                'rows': 4,
            }),
        }
        labels = {
            'rating': '⭐ Your Rating',
            'review_message': '💬 Your Review',
        }
