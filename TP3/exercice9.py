# Création d'un classe
class Personne:
    def afficher_infos(self):
        print("Nom : ", self.nom)
        print("Age : ", self.age, "ans")

# Phase de test

# Création d'une instance ou d'un objet de la classe Personne
p1 = Personne()

# Initialisation des attributs
p1.nom = "Alice"
p1.age = 30

# Appel de la méthode pour afficher les informations
p1.afficher_infos()
