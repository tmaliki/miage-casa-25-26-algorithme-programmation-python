# ======================
# TP1 - Exercice 14
# ======================

# Tri par sélection (Croissant : du plus petit au plus grand)
def tri_par_selection(liste):
    n = len(liste) 

    # Première boucle
    for i in range(n - 1):
        min_index = i

        # Deuxième boucle
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]: # Condition pour chercher l'index du plus pétit que min_index
                min_index = j
        
        # Echange
        if min_index != i:
            liste[i], liste[min_index] = liste[min_index], liste[i]
    
    return liste

# test [9, 3, 6, 1, 2]
tab = [9, 3, 6, 1, 2]
print("Liste avant le tri :", tab)
print("Liste après le tri :", tri_par_selection(tab))