# ======================
# TP1 - Exercice 10
# ======================
# Converstion d'un nombre décimal en binaire
def decimal_to_binary(n):
    if n == 0:
        return "0"

    restes = [] # pour stocker les restes

    while n > 0:
        restes.append(n % 2) # stocker le reste de la division par 2
        n //= 2 # stocker la partie entière de la division par 2

    restes.reverse() # inverser la liste des restes pour obtenir le bon ordre

    return ''.join(str(bit) for bit in restes)

# Phase de test
nombre = int(input("Saisissez un entier positif : "))
while nombre < 0:
    nombre = int(input("Veuillez entre un entier positif : "))

print(f"{nombre} (base 10) = {decimal_to_binary(nombre)} (base 2)")