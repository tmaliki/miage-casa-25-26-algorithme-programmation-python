# ======================
# TP1 - Exercice 9
# ======================
# Calcule du factorielle d'un entier positif
def factorielle(n):
    fact = 1 # initialisation à 1
    for i in range(1, n+1):
        fact *= i
    
    return fact

# Phase de test
n = int(input("Saisissez un entier positif : "))
while n < 0:
    n = int(input("Veuillez entre un entier positif : "))

print(f"Factorielle de n ({n}!) = {factorielle(n)}")