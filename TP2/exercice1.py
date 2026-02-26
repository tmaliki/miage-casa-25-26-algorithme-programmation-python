# Exercice 1
# Déclaration de la fonction somme
def somme(a: float, b: float) -> float:
    """
    Calcule et retourne la somme de deux nombres.
    Les paramètres a et b sont des nombres réels.
    """
    return a + b

# Phase de test de la fonction
nombre1 = float(input("Veuillez entrer le premier nombre : "))
nombre2 = float(input("Veuillez entrer le deuxième nombre : "))
resultat = somme(nombre1, nombre2)
print("La somme de", nombre1, "+", nombre2, "=", resultat)
print(f"{nombre1} + {nombre2} = {resultat:.2f}")
