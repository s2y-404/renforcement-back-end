from django.db import models
from .editeur import Editeur

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    résumé = models.TextField()
    date_de_publication = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    nombre_de_pages = models.IntegerField()
    langue = models.CharField(max_length=100)
    image_de_couverture = models.ImageField(upload_to='couvertures_livres/', null=True, blank=True)
    editeur = models.ForeignKey(Editeur, on_delete=models.SET_NULL, null=True)
    format = models.CharField(max_length=50)
    auteurs = models.ManyToManyField('Auteur', related_name='livres')
    categories = models.ManyToManyField('Categorie', related_name='livres')

    def __str__(self):
        return self.titre
