from django import forms 
from .models import Evenement

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = [
          'titre',
          'description',
          'date',
          'heure',
          'lieu',
          'image',
          'statut',  
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={'type':'date'}
            ),
            'heure': forms.TimeInput(
                attrs={'type':'time'}
            )
        }