# ======================
# TP1 - Exercice 2
# ======================

# 1. Déclaration de la fonction pairImpair
def pairImpair(n):
    if n % 2 == 0:
        return f"Le nombre {n} est Pair"
    else:
        return f"Le nombre {n} est Impair"

# 2. Déclaration de la fonction nombrePlusGrand
def nombrePlusGrand(n1, n2):
    if n1 > n2:
        return f"{n1} est plus grand entre ({n1} et {n2})"
    else:
        return f"{n2} est plus grand entre ({n1} et {n2})"

# 3. Déclaration de la fonction nombrePlusPetit
def nombrePlusPetit(nb1, nb2, nb3):
    min = nb1  # on suppose que nb1 est le plus petit

    # comparons les autres nombres avec le min supposé
    if nb2 < min:
        min = nb2  # ici nb2 devient le plus petit
    
    if nb3 < min:
        min = nb3  # ici nb3 devient le plus petit
    
    return f"Le plus petit entre ({nb1}, {nb2}, {nb3}) est {min}"

# Test des fonctions

# Test de la fonction pairImpair
# a = int(input("Saisissez un nombre : "))
# print(pairImpair(a)) # affichage et appel de la fonction pairImpair

# Test de la fonction nombrePlusGrand
# n1 = float(input("Saisissez le premier nombre : "))
# n2 = float(input("Saisissez le deuxième nombre : "))
# print(nombrePlusGrand(n1, n2))

# Test de la fonction nombrePlusPetit
nb1 = float(input("Saisissez le premier nombre : "))
nb2 = float(input("Saisissez le deuxième nombre : "))
nb3 = float(input("Saisissez le troisième nombre : "))
resultat = nombrePlusPetit(nb1, nb2, nb3) # recupération du résultat
print(resultat) # affichage du résultat