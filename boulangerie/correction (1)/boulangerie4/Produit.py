class Produit:
    def __init__(self, nom, prixDeRevient, prixDeVente):
        self.nom = nom
        self.prixDeRevient = prixDeRevient
        self.prixDeVente = prixDeVente
        print(
            f"{self.nom} est un produit ({self.prixDeRevient:.2f} / {self.prixDeVente:.2f})")
