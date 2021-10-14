from django import forms

class MyForm(forms.Form):
    first_number = forms.FloatField()
    operation = forms.CharField()
    second_number = forms.FloatField()
    
