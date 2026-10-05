from django.db import models
from utilisateurs.models import Utilisateur


class Notification(models.Model):
    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    TYPE_CHOICES = [
        ('evenement', 'Événement'),
        ('annonce', 'Annonce'),
        ('general', 'Général'),
    ]

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='general'
    )

    lu = models.BooleanField(default=False)

    date_creation = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.utilisateur} - {self.message[:30]}"
