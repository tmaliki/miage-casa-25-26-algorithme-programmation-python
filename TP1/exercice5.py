# ======================
# TP1 - Exercice 5
# ======================

nombre = int(input("Entrez un nombre entier positif : "))

while nombre < 0:
    print("Le nombre doit être positif.")
    nombre = int(input("Veuillez entrez un nombre entier positif : "))

# Affichage de l'entier positif saisi
print(f"Vous avez saisi le nombre positif : {nombre}")