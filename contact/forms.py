from django import forms
from .models import Contact

class NewContact(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['location']