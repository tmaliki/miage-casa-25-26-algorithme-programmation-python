def calcul_carre():
    try:
        n = int(input("Entrez un nombre entier : "))
        
        # calcule du carré
        # carre = n * n
        carre = n ** 2

        print("Le carré de", n, "est", carre)
    except ValueError:
        print("Erreur : entrée invalide.")

# appel de la fonction
calcul_carre()