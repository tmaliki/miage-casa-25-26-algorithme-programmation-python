# Ouverture du fichier en lecture seule
fichier = open("message.txt", "r")

# recupérarion du contenu du fichier
contenu = fichier.read()

# Affichage du contenu
print(contenu)

# Fermeture du fichier
fichier.close()