from Boulanger import *
from Patisserie import *


class Patissier(Boulanger):
    def __init__(self, prenom):
        super().__init__(prenom)
        print(f"{self.prenom} est également un pâtissier")

    def fabriquer(self, produit, quantite):
        print("En pâtisserie" if isinstance(produit, Patisserie) else "En boulangerie", end=", ")
        super().fabriquer(produit, quantite)
