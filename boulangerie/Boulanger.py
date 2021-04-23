from Fabrication import *
class Boulanger:
    def __init__(self, prenom):
        self.prenom=prenom
        self.fabrications = []
        self.vendeuses = []
        print(self.prenom+" est un boulanger")

    def fabriquer(self, produit, qty):
        self.fabrications.append(Fabrication(produit, qty))
        print(self.prenom + " fabrique " + str(qty) + " " + produit.nom)

    def embaucher(self, vendeuse):
        self.vendeuses.append(vendeuse)
        print(f"{self.prenom} embauche {vendeuse.prenom}")

    def editerBilan(self):
        print(f"BILAN")
        print(f"        Fabrications de {self.prenom}")
        totalFabrications = 0
        totalVentes = 0

        for fabrication in self.fabrications:
            produit = fabrication.produit
            totalLigne = fabrication.qty*produit.prixRevient
            totalFabrications += totalLigne
            print(f"        {fabrication.qty} {produit.nom} X {produit.prixRevient:.2f} = {totalLigne:.2f}")
        print(f"    TOTAL = {totalFabrications:.2f}")

        for vendeuse in self.vendeuses:
            print(" Ventes de " + vendeuse.prenom)
            totalVendeuse = 0
            for vente in vendeuse.ventes:
                produit = vente.produit
                totalLigne = vente.qty * produit.prixVente
                totalVendeuse += totalLigne
                print(f"        {vente.qty} {produit.nom} X {produit.prixVente:.2f} = {totalLigne:.2f}")
            print(f"   TOTAL = {totalVendeuse:.2f}")
            totalVentes += totalVendeuse

        print("     Totaux")
        print("     Fabrications = {:.2f}".format(totalFabrications))
        print("     Ventes = {:.2f}".format(totalVentes))
        print("     Ventes = {:+.2f}".format(totalVentes - totalFabrications))

