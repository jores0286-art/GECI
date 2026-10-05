from django import forms
from .models import Annonce


class AnnonceForm(forms.ModelForm):

    class Meta:
        model = Annonce

        fields = [
            'titre',
            'contenu',
            'statut',
        ]

        widgets = {
            'titre': forms.TextInput(
                attrs={
                    'placeholder': 'Titre de l’annonce'
                }
            ),

            'contenu': forms.Textarea(
                attrs={
                    'placeholder': 'Écrivez le contenu de l’annonce...'
                }
            ),
        }