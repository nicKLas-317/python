from Employe import *
from Fabrication import *


class Boulanger(Employe):
    def __init__(self, prenom):
        super().__init__(prenom)
        self.fabrications = []
        print(f"{self.prenom} est un boulanger")

    def fabriquer(self, produit, quantite):
        self.fabrications.append(Fabrication(produit, quantite))
        print(f"{self.prenom} fabrique {quantite} {produit.nom}")
