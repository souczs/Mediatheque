from django.db import models
from django.utils import timezone

# Create your models here.
class Membre(models.Model):
    name = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    dateEmprunt = models.DateTimeField(null=True, blank=True)
    emprunteur = models.ForeignKey(Membre, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.emprunteur and not self.dateEmprunt:
            self.disponible = False
            self.dateEmprunt = timezone.now()
            
        elif not self.emprunteur:
            self.disponible = True
            self.dateEmprunt = None
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Livre(Media):
    auteur = models.CharField(max_length=100)

class Dvd(Media):
    realisateur = models.CharField(max_length=100)

class Cd(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(Media):
    createur = models.CharField(max_length=100)