from django.db import models


class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='evenements/',
        blank=True,
        null=True

    )

    STATUT_CHOICES = [
        ('a_venir', 'À venir'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    ]

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='a_venir'
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.titre