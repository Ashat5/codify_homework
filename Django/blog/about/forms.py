from django import forms
from about.models import About

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

