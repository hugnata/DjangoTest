from django.db import models

# Create your models here.
from django.db.models.base import ModelBase


class Entreprise(models.Model):
    nom = models.CharField("Nom de l'entreprise",max_length=100)
    datecreation = models.DateField("Date de création",null=True)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    nom = models.CharField("Nom de l'employé", max_length=100)
    entreprise = models.ForeignKey("Entreprise", max_length=100, on_delete=models.CASCADE,related_name="employes")

    def __str__(self):
        return self.nom
