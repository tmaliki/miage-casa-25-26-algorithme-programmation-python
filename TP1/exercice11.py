# ======================
# TP1 - Exercice 11
# ======================

# fonction pour vérifier si un nombre est premier
def est_premier(n):
    # tous nolmbres < à 2 n'est pas premier
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# fonction pour afficher tous les nombres premiers <= N
def affichage_nbr_premiers(n):
    for j in range(2, n+1):
        if est_premier(j):
            print(j, end=" ")

# Test
nombre = int(input("Veuillez siasir un entier : "))
affichage_nbr_premiers(nombre)