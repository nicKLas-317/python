from Employe import *
from Boulanger import *
from Vendeuse import *


class Boulangerie:
    def __init__(self, nom):
        self.nom = nom
        self.employes = []
        print(f"{self.nom} est une boulangerie")

    def embaucher(self, employe):
        self.employes.append(employe)
        print(f"{self.nom} embauche {employe.prenom}")

    def editerBilan(self):
        boulangers = []
        vendeuses = []
        for employe in self.employes:
            if isinstance(employe, Boulanger):
                boulangers.append(employe)
            elif isinstance(employe, Vendeuse):
                vendeuses.append(employe)
        print("BILAN")
        totalFabrications = totalVentes = 0
        for boulanger in boulangers:
            print(f"  Fabrications de {boulanger.prenom}")
            totalBoulanger = 0
            for fabrication in boulanger.fabrications:
                produit = fabrication.produit
                totalLigne = fabrication.quantite*produit.prixDeRevient
                totalBoulanger += totalLigne
                print(
                    f"    {fabrication.quantite} {produit.nom} x {produit.prixDeRevient:.2f} = {totalLigne:.2f}")
            print(f"    Total = {totalBoulanger:.2f}")
            totalFabrications += totalBoulanger
        for vendeuse in vendeuses:
            print(f"  Ventes de {vendeuse.prenom}")
            totalVendeuse = 0
            for vente in vendeuse.ventes:
                produit = vente.produit
                totalLigne = vente.quantite*produit.prixDeVente
                totalVendeuse += totalLigne
                print(
                    f"    {vente.quantite} {produit.nom} x {produit.prixDeVente:.2f} = {totalLigne:.2f}")
            print(f"    Total = {totalVendeuse:.2f}")
            totalVentes += totalVendeuse
        print("  Totaux")
        print(f"    Fabrications = {totalFabrications:.2f}")
        print(f"    Ventes = {totalVentes:.2f}")
        print(f"    Résultat = {totalVentes-totalFabrications:+.2f}")
