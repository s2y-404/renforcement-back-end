from django.db import models
from .livre import Livre

class Exemplaire(models.Model):
    état = models.CharField(max_length=50)
    date_acquisition = models.DateField()
    localisation = models.CharField(max_length=100)
    disponibilité = models.BooleanField(default=True)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    def __str__(self):
        return f"self.localisation"
