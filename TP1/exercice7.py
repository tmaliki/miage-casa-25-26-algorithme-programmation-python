# ======================
# TP1 - Exercice 7
# ======================
# 1. calculer la somme des nombre pairs d'un tableau
def somme_tab_elt(tab):
    somme = 0
    for elt in tab:
        if elt % 2 == 0:
            somme += elt
    return somme

# test
liste = [6, 8, 1, 7, 10, 5, 3]
print(f"Somme des elemets = {somme_tab_elt(liste)}")

# 2. Recherche d'un élement dans la liste
def recherche_element(tab, x):
    trouve = False

    for i in range(len(tab)):
        if tab[i] == x:
            print("Element trouvé à la position :", i+1)
            trouve = True
            break
    
    if not trouve:
        print(f"Element non trouvé dans la liste")

# test 
elt_recherche = int(input("Saisissez l'élément à rechercher : "))
recherche_element(liste, elt_recherche)