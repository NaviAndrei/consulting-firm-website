from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'company', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Basic email validation
        if not email or '@' not in email:
            raise forms.ValidationError('Please enter a valid email address.')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # Basic phone number validation (optional field)
        if phone:
            # Remove non-numeric characters
            phone_digits = ''.join(filter(str.isdigit, phone))
            if len(phone_digits) < 10:
                raise forms.ValidationError('Please enter a valid phone number.')
        return phone