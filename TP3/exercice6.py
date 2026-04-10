# Exercice 6
def division_securisee(a, b):
    try:
        # Traitement
        result = a / b
        print(f"{a} / {b} = {result}")

    except ZeroDivisionError:
        # Gestion de l'erreur de division par zéro
        print("Erreur : Division par zéro")

    except ValueError:
        # Gestion des erreurs de type de données
        print("Erreur : Type de données invalide")

# Phase de test
division_securisee(28, 2)
division_securisee(28, 0)
division_securisee(28, "a")
