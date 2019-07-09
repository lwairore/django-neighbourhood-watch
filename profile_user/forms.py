from django import forms
from .models import Profile

class NewProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']
        widget = {
            'neighbourhood_id': forms.SelectMultiple(),
        }

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id', 'image']
        widget = {
            'neighbourhood_id': forms.SelectMultiple(),
        }
