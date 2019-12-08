from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class' : 'input-form-django'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'input-form-django'}))

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'input-form-django'}))
    email = forms.EmailField(label="E-mail", max_length=100, widget=forms.TextInput(attrs={'class' : 'input-form-django'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-form-django'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input-form-django'}))
