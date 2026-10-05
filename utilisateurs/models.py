from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)

    ROLE_CHOICES = [
        ('administrateur', 'Administrateur'),
        ('organisateur', 'Organisateur'),
        ('employe', 'Employé'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='employe'
    )

    date_inscription = models.DateTimeField(auto_now_add=True)
    models.DateField(auto_now_add=True)


    def str(self):
        return f"{self.prenom} {self.nom}"