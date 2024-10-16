from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    prénom = models.CharField(max_length=255)
    date_de_naissance = models.DateField()
    
    def __str__(self):
        return self.titre
