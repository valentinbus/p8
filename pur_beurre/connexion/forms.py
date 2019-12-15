from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class' : 'input-form-django'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'input-form-django'}))

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class' : 'input-form-django'}))
    email = forms.EmailField(label="Adresse mail", max_length=100, widget=forms.TextInput(attrs={'class' : 'input-form-django'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class' : 'input-form-django'}))
    confirm_password = forms.CharField(label="Confirmez votre mot de passe", widget=forms.PasswordInput(attrs={'class' : 'input-form-django'}))
