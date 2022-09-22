from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import *


class DatePickerInput(forms.DateInput):
        input_type = 'date'
class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class ContactForm (ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name','last_name', 'address', 'email', 'phone_number', 'date_time', 'notes']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Your last name'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder':'Your address'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder':'Your email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder':'Your phone number'}),
            'date_time': DatePickerInput(attrs={'class': 'form-control', 'placeholder':'Your last name'}),
            'notes': Textarea(attrs={'class': 'form-control', 'placeholder':'Any info that may help us plan your experience to the maximum?'}),
        }