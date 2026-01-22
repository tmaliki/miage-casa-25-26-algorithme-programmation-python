# ======================
# TP1 - Exercice 6
# ======================

# 1. Affichage des nombre de 1 à 20 et arrêt à 13
def nombre1A20Stop13():
    print("Affichage des nombres de 1 à 20 et arrêt à 13 :")
    for i in range(1, 21):
        if i == 13:
            break      # sortie de force de la boucle
        print(i)
    print("***********************")

# 2. Affichage des nombres immpairs de 1 à 20
def nombreImpair1A20():
    print("Affichage des nombres impairs de 1 à 20 :")
    for i in range(1, 21):
        if i % 2 == 0:
            continue
        print(i)
    print("***********************")

# Phase de test
nombre1A20Stop13() # 1
nombreImpair1A20() # 2