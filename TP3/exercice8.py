def lire_fichier_securise():
    # initialisation de la variable fichier
    fichier = None

    try:
        # ouverture du fichier en mode lecture
        fichier = open("exercice8.py", "r")

        # lecture du fichier
        contenu = fichier.read()

        # affichage du contenu
        print(contenu)

    except FileNotFoundError:
        print("Erreur : Fichier non trouvé.")

    finally:
        if fichier is not None:
            fichier.close()
            print("Fichier fermé correctement grâce au bloc finally.")
        else:
            print("Aucun fichier fermer.")

# appel de la fonction
lire_fichier_securise()

# Solution pro
def lire_fichier_securise_pro():
    try:
        # ouverture du fichier en mode lecture
        with open("exercice9.py", "r") as fichier:
            # lecture du fichier
            contenu = fichier.read()

            # affichage du contenu
            print(contenu)

    except FileNotFoundError:
        print("Erreur : Fichier non trouvé.")

    finally:
        print("Opération terminée.")