# ======================
# TP1 - Exercice 8
# ======================
# Element le plus fréquent avec dictionnaire
def nombre_occurences(liste):
    freq = {}

    # Comptons des occurences
    for x in liste:
        if x in freq:
            freq[x] += 1 # Pour les éléments déjà vus
        else:
            freq[x] = 1 # Première fois que l'élément apparaît

    # Trouvons l'élément le plus fréquent
    max_freq = 0
    element = liste[0]
    for k in freq:
        if freq[k] > max_freq:
            max_freq = freq[k]
            element = k

    print(f"Element le plus fréquent : {element}")
    print(f"Nombre d'occurences : {max_freq}")

# Phase de test
liste = [5, 2, 8, 5, 3, 2, 5, 8, 8, 9, 8]
nombre_occurences(liste)