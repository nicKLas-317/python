class Produit:
    def __init__(self, nom, prixRevient, prixVente):
        self.nom = nom
        self.prixRevient = prixRevient
        self.prixVente = prixVente
        print(f"{self.nom} est un produit ({self.prixRevient:.2f} / {self.prixVente:.2f})")