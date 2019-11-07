from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import ConnexionForm, RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profil
from django.contrib.auth.models import User

from pprint import pprint


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
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    pprint(f'LOCALS===>{locals()}')
    return render(request, 'auth/connexion.html', locals())

#@login_required(login_url="/connexion")
def deconnexion(request):
    """
    Logout user
    """
    logout(request)
    return render(request, "auth/deconnexion.html")

def registration(request):
    """
    Registration part for new user
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        pprint(f"form =={form}")
        pprint(f"form =={form.cleaned_data}")
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            """
            ToDo 
            if user not in DB create user with these fields
            - check user in db 
            - Redirect to connexion page when it's done
            """
            if User.objects.filter(username=username):
                print('username already exists')
            else:
                if password==confirm_password:
                    User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
        else:
            form = RegistrationForm()
            print("false")

    return render(request, 'auth/registration.html', locals())

def test(request):
    user = User.objects
    if user.filter(username="valentin"):
        print('ok')
    print(user)
    return HttpResponse(user)
