from django.shortcuts import render, redirect
from .models import Annonce
from .forms import AnnonceForm


def liste_annonces(request):

    annonces = Annonce.objects.filter(
        statut='publiee'
    ).order_by('-date_publication')

    return render(
        request,
        'annonces/liste.html',
        {'annonces': annonces}
    )


def creer_annonce(request):

    if request.method == 'POST':
        form = AnnonceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('liste_annonces')

    else:
        form = AnnonceForm()

    return render(
        request,
        'annonces/formulaire.html',
        {'form': form}
    )