from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import ConnexionForm
from django.urls import reverse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


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

    print(locals())
    return render(request, 'connexion/connexion.html', locals())

@login_required(login_url="/connexion")
def deconnexion(request):
    """
    Logout user
    """
    logout(request)
    reverse("connexion")
    return HttpResponseRedirect('/connexion')

@login_required(login_url="/connexion")
def dire_bonjour(request):
    if request.user.is_authenticated:
        return HttpResponse("Salut, {0} !".format(request.user.username))
    return HttpResponse("Salut")
