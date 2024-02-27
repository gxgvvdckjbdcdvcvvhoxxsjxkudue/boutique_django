from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CompteUtilisateur
from django.contrib import messages

# Create your views here.

# fonction pour la page d'inscription  
def InscriptionPage(request):
    form = CompteUtilisateur()
    if request.method == 'POST':
        form = CompteUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


# fonction pour la page de connexion
def ConnexionPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, "Nom d'utilisateur ou mot de passe incorecte")
    return render(request, 'compte/connexion.html')

def Deconnexion(request):
    logout(request)
    return redirect('connexion')