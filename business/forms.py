from django import forms
from .models import Business

class NewBusiness(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user_id', 'neighbourhood_id']