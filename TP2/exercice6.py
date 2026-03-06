# Exercice 6
# liste : [3, 2, 5, 7, 8]
# liste_carre = [9, 4, 25, 49, 64]

def carre_liste_nbr(tab):
    tab_carre = list(map(lambda elt: elt ** 3, tab))
    return tab_carre

# Phase de test
liste = [3, 2, 5, 7, 8, 4, 3, 9]
print("Liste des carrés : ", carre_liste_nbr(liste))