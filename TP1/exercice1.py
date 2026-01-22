# ======================
# TP1 - Exercice 1
# ======================

# 1. Somme de deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
somme = a + b
print("La somme de ", a, " + ", b, " = ", somme)

# Affichage formaté
print(f"La somme de {a} + {b} = {somme}")

# 2. Calcul de l'aire d'un rectangle
longueur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
aire = longueur * largeur
print(f"Aire du rectangle {longueur} x {largeur} = {aire}")

# 3. Moyenne de trois nombres
nbr1 = float(input("Entrez le premier nombre : "))
nbr2 = float(input("Entrez le deuxième nombre : "))
nbr3 = float(input("Entrez le troisième nombre : "))
moyenne = (nbr1 + nbr2 + nbr3) / 3
print(f"La moyenne de {nbr1}, {nbr2} et {nbr3} = {moyenne}")

# 4. Calcul de l'âge
from datetime import datetime # import de l'objet datetime
annee_naiss= int(input("Entrez votre année de naissance : "))
annee_actuelle = datetime.now().year # obtention de l'année actuelle
age = annee_actuelle - annee_naiss
print(f"Vous avez {age} ans en {annee_actuelle}.")