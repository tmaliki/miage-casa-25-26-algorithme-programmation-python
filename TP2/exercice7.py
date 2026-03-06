# Exercice 7
# liste : [7, 6, 8, 9, 2, 4, 5]
# liste_pair : [6, 8, 2, 4]

def liste_nbr_pair(tab):
    return list(filter(lambda elt: elt % 2 == 0, tab))

# Phase de test
liste = [7, 6, 8, 9, 2, 4, 5]
print("Liste des nombres pairs : ", liste_nbr_pair(liste))