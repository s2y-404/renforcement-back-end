from django.db import models
from django.contrib.auth.models import User

from renforcementbackend.models.livre import Livre

class Emprunt(models.Model):
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prévue = models.DateTimeField()
    date_retour_effective = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('en_retard', 'En retard'),
    ])
    remarques = models.TextField(null=True, blank=True)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='emprunt_livre')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprunt_user', null=True)

    def __str__(self):
        return self.date_emprunt
