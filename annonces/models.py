from django.db import models


class Annonce(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()

    STATUT_CHOICES = [
        ('brouillon', 'Brouillon'),
        ('publiee', 'Publiée'),
    ]

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='brouillon'
    )

    date_publication = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.titre
