from django.urls import path
from . import views


urlpatterns = [
    path('', views.liste_annonces, name='liste_annonces'),
    path('nouvelle/', views.creer_annonce, name='creer_annonce'),
]