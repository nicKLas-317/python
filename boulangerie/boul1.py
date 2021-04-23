from Boulanger import *
from Vendeuse import *
from Produit import *
# --------------------------------------------------
bernard = Boulanger("Bernard")
violaine = Vendeuse("Violaine")
virginie = Vendeuse("Virginie")
baguette = Produit("baguette", 0.10, 0.78)
croissant = Produit("croissant", 0.15, 1.10)
painDeMie = Produit("pain de mie", 0.35, 2.50)
bernard.embaucher(violaine)
bernard.embaucher(virginie)
bernard.fabriquer(baguette, 80)
bernard.fabriquer(croissant, 60)
bernard.fabriquer(painDeMie, 20)
violaine.vendre(baguette, 75)
violaine.vendre(croissant, 50)
virginie.vendre(painDeMie, 20)
bernard.editerBilan()
