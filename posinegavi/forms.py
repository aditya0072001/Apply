from django import forms

class CheckForm(forms.Form):
    text=forms.CharField(max_length=38,required=True)
    
    