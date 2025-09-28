# dishes/forms.py

from django import forms
from django.utils import timezone
from .models import Reservation

class ReservationForm(forms.ModelForm):
    """Form for handling table reservations with validation"""
    
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'guests', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number (optional)'
            }),
            'guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '20'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            })
        }
    
    def clean_date(self):
        """Validate that reservation date is not in the past"""
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise forms.ValidationError("Reservation date cannot be in the past.")
        return date
    
    def clean_guests(self):
        """Validate number of guests"""
        guests = self.cleaned_data.get('guests')
        if guests is not None and guests < 1:
            raise forms.ValidationError("Number of guests must be at least 1.")
        if guests is not None and guests > 20:
            raise forms.ValidationError("Maximum 20 guests per reservation.")
        return guests
