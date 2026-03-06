# Exercice 8

# Définition d'un dictionnaire
etudiants = {
    "Alice": 15.65,
    "Bob": 12.32,
    "Charlie": 13.45,
    "David": 14.56
}
# etudiants[Bob]

def rechercher_note_etudiant(nom, data):
    if nom in data:
        print(f"Note de {nom} : {data[nom]}")
    else:
        print(f"Etudiant {nom} non trouvé.")

# Phase de test
nom_etudiant = input("Entrez le nom de l'étudiant : ")
rechercher_note_etudiant(nom_etudiant, etudiants)
