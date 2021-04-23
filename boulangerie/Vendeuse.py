from Vente import *


class Vendeuse:
    def __init__(self, prenom):
        self.prenom=prenom
        self.ventes = []
        print(f"{self.prenom}  est une vendeuse")

    def vendre(self, produit, qty):
        self.ventes.append(Vente(produit, qty))
        print(self.prenom + " vend " + str(qty) + " " + produit.nom)