# ======================
# TP1 - Exercice 12
# ======================

# Trouvons le PGCD de deux nombre a et b
def pgcd(a, b):
    a = abs(a) # On prend la valeur absolue de a
    b = abs(b) # On prend la valeur absolue de b

    while b != 0:
        r = a % b
        a = b
        b = r

    return a

# Test
nbrA = int(input("Entrez le premier nombre: "))
nbrB = int(input("Entrez le deuxième nombre: "))
print(f"Le PGCD({nbrA}, {nbrB}) = {pgcd(nbrA, nbrB)}")