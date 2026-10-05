from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('evenements/', views.liste_evenements, name='liste_evenements'),
    path('nouveau/',
         views.creer_evenement, name='creer_evenement'),
]