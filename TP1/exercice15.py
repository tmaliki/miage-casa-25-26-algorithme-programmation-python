# ======================
# TP1 - Exercice 15
# ======================

import random

# Tri par insertion
def tri_par_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]

        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        
        liste[j + 1] = cle
    
    return liste

# Génération de la liste
n = int(input("Entrez la taille de la liste : "))
tableau = []
for i in range(n):
    tableau.append(random.randint(1, 100))

# Affichage de la liste avant et après le tri
print("Liste avant le tri :", tableau)
print("Liste après le tri", tri_par_insertion(tableau))