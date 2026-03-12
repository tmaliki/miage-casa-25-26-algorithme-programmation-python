# Gestion des étudiants (mini-système)

# Liste des étudiants
etudiants = []

# Pile pour l'historique des actions
historique = []

# Fonction pour ajouter un étudiant
def ajouter_etudiant(nom, note):
    etudiants.append({"nom": nom, "note": note})
    historique.append(f"Ajout de l'étudiant {nom} avec la note {note}")

# Fonction pour calculer la moyenne
def moyenne_notes():
    notes = list(map(lambda e: e["note"], etudiants))
    moy = sum(notes) / len(notes)
    return f"{moy:.2f}"

# Fonction récupérer la liste des admins
def etudiants_admins():
    return list(filter(lambda e: e["note"] >= 10, etudiants))

# Fonction pour trier les étudiants par note
def trier_par_note():
    return sorted(etudiants, key=lambda e: e["note"], reverse=True)

# Phase de test

# Ajout des étudiants
ajouter_etudiant("Ali", 14)
ajouter_etudiant("Sophie", 12)
ajouter_etudiant("Tom", 9)
ajouter_etudiant("Emma", 15)
ajouter_etudiant("Liam", 8)

# Affichage
print("Moyenne : ", moyenne_notes())
print("Étudiants admis : ", etudiants_admins())
print("Triés par note : ", trier_par_note())
print("Historique des actions : ", historique)
