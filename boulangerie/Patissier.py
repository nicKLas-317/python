from Boulanger import *
from Fabrication import *
from Patisserie import *

class Patissier(Boulanger):
    def __init__(self, prenom):
        super().__init__(prenom)
        self.fabrications = []
        print(self.prenom+" est également un pâtissier")

    def fabriquer(self, produit, qty):
        if isinstance(produit, Patisserie):
            print("En pâtisserie, " + self.prenom + " fabrique " + str(qty) + " " + produit.nom)
        else:
            print("En boulangerie, " + self.prenom + " fabrique " + str(qty) + " " + produit.nom)
        super().fabriquer(produit, qty)