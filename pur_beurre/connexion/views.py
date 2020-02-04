from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import ConnexionForm, RegistrationForm, ForgotPasswordForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profil
from django.contrib.auth.models import User
import logging


logging.basicConfig(level=logging.DEBUG)


def connexion(request):
    """
    form to connect to the platform
    """
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                username=username,
                password=password
            )
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'auth/connexion.html', locals())


@login_required(login_url="/connexion")
def deconnexion(request):
    """
    Logout user
    """
    logout(request)
    response = "Vous vous êtes bien déconnecté"
    return render(request, "auth/validation_page.html", locals())


def registration(request):
    """
    Registration part for new user
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if User.objects.filter(username=username):
                return render(
                    request,
                    'auth/registration_confirmation.html',
                    {'response': "Cet utilisateur existe déjà"}
                )

            else:
                if password == confirm_password:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    response = "Vous vous êtes bien enregistré"
                    return render(
                        request,
                        'auth/registration_confirmation.html',
                        {'response': "Votre utilisateur a bien été enregistré"}
                    )

    else:
        form = RegistrationForm()

    return render(request, 'auth/registration.html', {'form': form})
