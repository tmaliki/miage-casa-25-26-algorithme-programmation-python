# Exercice 12

# Classe parent
class Vehicule:
    def __init__(self, marque):
        self.marque = marque
    
    def afficher(self):
        print(f"Marque : {self.marque}")

# Classe enfant : Voitire Hérite de Vehicule
class Voiture(Vehicule):
    def afficher_type(self):
        print("Type : Voiture")

# Phase de test
v = Voiture("Toyota")
v.afficher()
v.afficher_type()