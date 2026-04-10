# Exercice 3

# 1- Fonction pour ajouter du contenu dans un fichier
def ajout_contenu(contenu):
    # Ouvrir le fichier en mode ajout
    fichier = open("message.txt", "a")

    # Ajout d'une nouvelle ligne
    # fichier.write("\nLa programmation est passionnante")
    fichier.write(f"\n{contenu}")

    # Fermeture du fichier
    fichier.close()

# 2- Fonction pour lire/afficher le contenu d'un fichier
def lire_contenu():
    # Ouvrir le fichier en mode lecture
    fichier = open("message.txt", "r")

    # Lecture du contenu
    contenu = fichier.read()
    print(contenu)

    # Fermeture du fichier
    fichier.close()

# Phase de test
texte = input("Saisissez le texte à ajouter dans le fichier : ")
ajout_contenu(texte) # Ajout du texte dans le fichier

print("\nContenu du fichier après ajout :")
lire_contenu() # Lecture et affichage du contenu du fichier