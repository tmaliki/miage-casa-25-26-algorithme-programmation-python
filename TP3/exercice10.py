# Création d'un classe
class Personne:
    # Constructeur : initialisation des attributs
    def __init__(self, n, a):
        self.nom = n
        self.age = a

    def afficher_infos(self):
        print("Nom : ", self.nom)
        print("Age : ", self.age, "ans")

# Phase de test
john = Personne("John", 25)
sara = Personne("Sara", 30)

# Affichage des informations
john.afficher_infos()
print("\n--------------\n")
sara.afficher_infos()