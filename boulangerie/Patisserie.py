from Produit import *

class Patisserie(Produit):
    def __init__(self, nom, prixRevient, prixVente, auBeurre=False):
        super().__init__(nom, prixRevient, prixVente)
        self.auBeurre = auBeurre
        auBeurre = ' au beurre' if self.auBeurre else ''
        print(
            f"{self.nom} est plus précisément une pâtisserie{auBeurre}")