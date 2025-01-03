from django.shortcuts import render, redirect
from django.contrib import messages
from .models import utilisateur
from django.contrib.auth import authenticate, login

def accueil(request):
    context = {
        'title': 'Bienvenue sur la plateforme scolaire',
        'description': 'Cette plateforme permet aux étudiants et enseignants de collaborer efficacement, suivre des cours, et accéder à des ressources éducatives.',
    }
    return render(request, 'accueil.html', context)

def inscription(request):
    if request.method == 'POST':
        prenom = request.POST['prenom']
        nom = request.POST['nom']
        email = request.POST['email']
        mot_de_passe = request.POST['mot_de_passe']
        confirmer_mot_de_passe = request.POST['confirmer_mot_de_passe']

        if mot_de_passe != confirmer_mot_de_passe:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'inscription.html')

        # Enregistrer dans la base de données
        try:
            user = utilisateur(prenom=prenom, nom=nom, email=email, mot_de_passe=mot_de_passe)
            user.save()
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect('accueil')  # Remplacez 'home' par l'URL de votre page d'accueil
        except:
            messages.error(request, "Une erreur est survenue. Cet email est peut-être déjà utilisé.")
            return render(request, 'inscription.html')
    return render(request, 'inscription.html')




def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Champ du formulaire pour l'email
        password = request.POST.get('password')  # Champ du formulaire pour le mot de passe

        # Authentifier l'utilisateur
        user = authenticate(request, username=email, password=password)

        if user is not None:  # Si les identifiants sont corrects
            login(request, user)  # Connecter l'utilisateur
            return redirect('accueil')  # Redirige vers l'URL nommée 'accueil'
        else:
            # Identifiants invalides
            return render(request, 'login.html', {'error_message': 'Email ou mot de passe incorrect.'})

    # Afficher le formulaire de connexion pour les requêtes GET
    return render(request, 'login.html')


