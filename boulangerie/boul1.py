from Boulangerie import *
from Boulanger import *
from Patissier import *
from Vendeuse import *
from Produit import *
from Patisserie import *
# --------------------------------------------------
# laGrandeBoulangerie = Boulangerie("La Grande Boulangerie")
# bernard = Boulanger("Bernard")
# paul = Patissier("Paul")
# violaine = Vendeuse("Violaine")
# virginie = Vendeuse("Virginie")
# baguette = Produit("baguette", 0.10, 0.78)
# croissant = Produit("croissant", 0.15, 1.10)
# painDeMie = Produit("pain de mie", 0.35, 2.50)
# charlotte = Patisserie("charlotte", 6.20, 30.00, True)
# laGrandeBoulangerie.embaucher(bernard)
# laGrandeBoulangerie.embaucher(paul)
# laGrandeBoulangerie.embaucher(violaine)
# laGrandeBoulangerie.embaucher(virginie)
# bernard.fabriquer(baguette, 80)
# bernard.fabriquer(painDeMie, 20)
# paul.fabriquer(croissant, 60)
# paul.fabriquer(charlotte, 5)
# violaine.vendre(baguette, 75)
# violaine.vendre(croissant, 50)
# virginie.vendre(painDeMie, 20)
# virginie.vendre(charlotte, 4)
# laGrandeBoulangerie.editerBilan()

croissant = Produit("croissant", 0.15, 1.10)
painDeMie = Produit("pain de mie", 0.35, 2.50)
v1 = Vendeuse("v1")
v2 = Vendeuse("v2")
v3 = Vendeuse("v3")
v1.vendre(croissant, 50)
v1.vendre(painDeMie, 10)  #(CA = 80)
v2.vendre(painDeMie, 30)  #(CA = 75)
v3.vendre(croissant, 100) #(CA = 110)
vendeuses = sorted([v1, v2, v3])
for vendeuse in vendeuses:
  print(vendeuse, end = ", ") #v2, v1, v3