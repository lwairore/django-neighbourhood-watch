from django import forms
from .models import Events

class NewEvent(forms.ModelForm):
    class Meta:
        model = Events
        exclude = ['posted_at', 'location']