# forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.EmailField(max_length=100, label='Email')
    email = forms.CharField(label='Name')
    message = forms.CharField(widget=forms.Textarea, label='Message')
