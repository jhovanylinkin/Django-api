from django import forms

class Quest(forms.Form):
    ide = forms.CharField(max_length=12)
    name = forms.CharField(max_length= 123)