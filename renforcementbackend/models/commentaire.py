from django.db import models

class Commentaire(models.Model):
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    visible = models.BooleanField(default=True)
    modéré = models.BooleanField(default=False)
    livre = models.ForeignKey('Livre', on_delete=models.CASCADE, related_name='commentaires')

    def __str__(self):
        return self.contenu
