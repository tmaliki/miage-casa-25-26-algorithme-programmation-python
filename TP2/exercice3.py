# Exercice 3

x = 10    # variable globale
print("Valeur de x :", x)

def test_portee():
    x = 5    # variable locale
    print("Valeur de x à l'intérieur de la fonction :", x)

# Appel de la fonction
test_portee()

# Affichage de la valeur de x hors de la fonction
print("Valeur de x hors de la fonction :", x)