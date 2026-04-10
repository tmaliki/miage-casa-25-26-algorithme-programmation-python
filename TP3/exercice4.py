# Exercice 4

# Ouverture du fichie en mode lecture
fichier = open("message.txt", "r")

# Lecture de toutes les lignes dans une liste
lignes = fichier.readlines()

# Boucle
for i in range(0, len(lignes)):
    # Affichage de la ligne avec son numéro
    # strip() : supprime les espaces en début et fin de ligne
    print(i + 1, lignes[i].strip())

# fermeture du fichier
fichier.close()