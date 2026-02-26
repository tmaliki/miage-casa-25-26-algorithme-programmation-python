# Exercice 2
def afficher_message(nom: str) -> None:
    print(f"Bienvenu {nom} !")

# Phase de test de la fonction
votre_nom = input("Veuillez entrer votre nom : ")
afficher_message(votre_nom)