from Employe import *
from Vente import *


class Vendeuse(Employe):
    def __init__(self, prenom):
        super().__init__(prenom)
        self.ventes = []
        print(f"{self.prenom} est une vendeuse")

    def __str__(self):
        return self.prenom

    def __repr__(self):
        return self.prenom

    def __lt__(self, other):
        totalSelf = totalOther = 0
        for vente in self.ventes:
            totalSelf += vente.quantite*vente.produit.prixDeVente
        for vente in other.ventes:
            totalOther += vente.quantite*vente.produit.prixDeVente
        return totalSelf < totalOther

    def vendre(self, produit, quantite):
        self.ventes.append(Vente(produit, quantite))
        print(f"{self.prenom} vend {quantite} {produit.nom}")
