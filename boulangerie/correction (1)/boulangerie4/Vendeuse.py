from Employe import *
from Vente import *

class Vendeuse(Employe):
    def __init__(self, prenom):
        super().__init__(prenom)
        self.ventes = []
        print(f"{self.prenom} est une vendeuse")

    def vendre(self, produit, quantite):
        self.ventes.append(Vente(produit, quantite))
        print(f"{self.prenom} vend {quantite} {produit.nom}")
