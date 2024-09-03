from datetime import date
from django.db import models


# HYOFANG LUY MARSHALL
# DJOMATCHOUA WAMENI Ange Manuela
# DJEUMO LEUNA Jemima 


class Client(models.Model):
    id_cli = models.AutoField(primary_key=True)
    nom_cli = models.CharField(max_length=100)
    adr_cli = models.CharField(max_length=200)
    ville_cli = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_cli
    
class Melange(models.Model):
    id_melange = models.AutoField(primary_key=True)
    description = models.TextField()
    
    

class Pain(models.Model):
    id_pain = models.AutoField(primary_key=True)
    description = models.TextField()
    prix_pain_ht = models.DecimalField(max_digits=8, decimal_places=2)
    melange = models.ForeignKey(Melange, on_delete=models.CASCADE, related_name='pains')

    def __str__(self):
        return f"Pain {self.id_pain}: {self.description}"
    
    
class Approvisionnement(models.Model):
    melange = models.ForeignKey(Melange, on_delete=models.CASCADE, related_name='approvisionnements')
    semaine_appro = models.IntegerField()
    quantite_melange = models.PositiveIntegerField()

    def __str__(self):
        return f"Approvisionnement de {self.quantite_melange} unités du mélange {self.melange.id_melange} à la semaine {self.semaine_appro}"
    

    

class Livraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='livraisons')
    pain = models.ForeignKey(Pain, on_delete=models.CASCADE, related_name='livraisons')
    date_livraison = models.IntegerField()
    nombre_pains = models.PositiveIntegerField()

    def __str__(self):
        return f"Livraison de {self.nombre_pains} pains '{self.pain.description}' au client {self.client.nom} le {self.date_livraison}"