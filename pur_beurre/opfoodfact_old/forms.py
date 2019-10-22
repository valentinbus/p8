from django import forms

class NameForm(forms.Form):
    query = forms.CharField(label='', max_length=100)
    