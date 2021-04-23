from Boulanger import *
from Vendeuse import *


class Boulangerie:
    def __init__(self, nom):
        self.nom = nom
        self.employes = []
        self.ventes = []
        print(self.nom+" est une boulangerie")

    def embaucher(self, employe):
        self.employes.append(employe)
        print(f"{self.nom} embauche {employe.prenom}")

    def editerBilan(self):
        print(f"BILAN DE {self.nom}")
        totalFabrications = totalVentes = 0

        for employe in self.employes:
            if isinstance(employe, Boulanger):
                print(f"    Fabrications de {employe.prenom}")
                for fabrication in employe.fabrications:
                    produit = fabrication.produit
                    totalLigne = fabrication.qty * produit.prixRevient
                    totalFabrications += totalLigne
                    print(f"        {fabrication.qty} {produit.nom} X {produit.prixRevient:.2f} = {totalLigne:.2f}")
                print(f"        TOTAL = {totalFabrications:.2f}")
            elif isinstance(employe, Vendeuse):
                totalVendeuse = 0
                print(f"    Ventes de {employe.prenom}")
                for vente in employe.ventes:
                    produit = vente.produit
                    totalLigne = vente.qty * produit.prixVente
                    totalVendeuse += totalLigne
                    print(f"        {vente.qty} {produit.nom} X {produit.prixVente:.2f} = {totalLigne:.2f}")
                totalVentes += totalVendeuse
                print(f"        TOTAL = {totalVendeuse:.2f}")
        print("     Totaux")
        print("         Fabrications = {:.2f}".format(totalFabrications))
        print("         Ventes = {:.2f}".format(totalVentes))
        print("         Ventes = {:+.2f}".format(totalVentes - totalFabrications))