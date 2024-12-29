from django.contrib import admin
from .models import utilisateur  # Importer le modèle

@admin.register(utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')  # Colonnes à afficher dans l'admin
    search_fields = ('prenom', 'nom', 'email')  # Champs de recherche

# Register your models here.
