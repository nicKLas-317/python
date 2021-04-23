from Fabrication import *

class Boulanger():
    def __init__(self, prenom):
        self.prenom = prenom
        self.fabrications = []
        print(self.prenom+" est un boulanger")

    def fabriquer(self, produit, qty):
        self.fabrications.append(Fabrication(produit, qty))
        print(self.prenom + " fabrique " + str(qty) + " " + produit.nom)

    # def embaucher(self, vendeuse):
    #     self.vendeuses.append(vendeuse)
    #     print(f"{self.prenom} embauche {vendeuse.prenom}")


