# Exercice 10

# 1 - Simuler une pile avec une liste (append, pop)
pile = []
pile.append("Tâche 1")
pile.append("Tâche 2")
pile.append("Tâche 3")
pile.append("Tâche 4")

print("Pile après ajout de tâches :", pile)
print("Dernière tâche :", pile.pop())

print("Première tâche :", pile[0])

# 2 - Trier une liste de dictionnaires (étudiants) selon la note
# Tableau d'objets : une collection
etudiants = [
    {"nom": "Alice", "note": 14},
    {"nom": "Bob", "note": 17},
    {"nom": "Charlie", "note": 16},
    {"nom": "David", "note": 15}
]

# Tri des étudiants par note dans l'ordre croissant
etudiants_tries = sorted(etudiants, key=lambda elt: elt["note"])
print("Étudiants triés par note dans l'ordre croissant :", etudiants_tries)

# Tri des étudiants par note dans l'ordre décroissant
etudiants_tries_desc = sorted(etudiants, key=lambda elt: elt["note"], reverse=True)
print("Étudiants triés par note dans l'ordre décroissant :", etudiants_tries_desc)