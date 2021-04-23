from Produit import *


class Patisserie(Produit):
    def __init__(self, nom, prixDeRevient, prixDeVente, auBeurre=False):
        super().__init__(nom, prixDeRevient, prixDeVente)
        self.auBeurre = auBeurre
        auBeurre = ' au beurre' if self.auBeurre else ''
        print(
            f"{self.nom} est plus précisément une pâtisserie{auBeurre}")
