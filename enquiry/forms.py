from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['parent_name', 'child_name', 'child_age', 'phone', 'email', 'message']
        widgets = {
            'parent_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Parent's Full Name",
            }),
            'child_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Child's Full Name",
            }),
            'child_age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age in years',
                'min': 1,
                'max': 10,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any specific questions or requirements?',
                'rows': 4,
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone

    def clean_child_age(self):
        age = self.cleaned_data.get('child_age')
        if age and (age < 1 or age > 10):
            raise forms.ValidationError("Child age must be between 1 and 10 years.")
        return age
