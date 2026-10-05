from django.shortcuts import render, redirect
from .models import Evenement
from annonces.models import Annonce
from notifications.models import Notification
from utilisateurs.models import Utilisateur
from .forms import EvenementForm


def accueil(request):

    nombre_evenements = Evenement.objects.count()
    nombre_annonces = Annonce.objects.count()
    nombre_notifications = Notification.objects.count()
    nombre_utilisateurs = Utilisateur.objects.count()

    utilisateur = Utilisateur.objects.first()

    evenements_a_venir = Evenement.objects.filter(
        statut='a_venir'
    ).order_by('date', 'heure')[:4]

    annonces_recentes = Annonce.objects.filter(
        statut='publiee'
    ).order_by('-date_publication')[:4]

    contexte = {
        'nombre_evenements': nombre_evenements,
        'nombre_annonces': nombre_annonces,
        'nombre_notifications': nombre_notifications,
        'nombre_utilisateurs': nombre_utilisateurs,

        'utilisateur': utilisateur,

        'evenements_a_venir': evenements_a_venir,
        'annonces_recentes': annonces_recentes,
    }

    return render(
        request,
        'accueil.html',
        contexte
    )




def liste_evenements(request):

    evenements = Evenement.objects.all().order_by('date', 'heure')
    utilisateur = Utilisateur.objects.first()


    return render(
        request,
        'evenements/liste.html',
        {
            'evenements': evenements,
            'utilisateur': utilisateur,
            }
    )


def creer_evenement(request):

    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('liste_evenements')

    else:
        form = EvenementForm()

    return render(
        request,
        'evenements/formulaire.html',
        {'form': form}
    )