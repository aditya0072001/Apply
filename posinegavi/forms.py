from django import forms

class CheckForm(forms.Form):
    text=forms.CharField(required=True)
    
    