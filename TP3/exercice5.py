# Exercice 5

# Ouverture du fichier source en mode lecture
source = open("message.txt", "r")

# Ouverture du fichier de destination en mode écriture
destination = open("copie.txt", "w")

# lecture du fichier source
contenu = source.read()

# Ecriture du contenu dans le fichier de destination
destination.write(contenu)

# Fermeture des deux fichiers
source.close()
destination.close()
