# ======================
# TP1 - Exercice 4
# ======================

# 1. Affichages des 5 premiers multiples d'un nombre
def cinq_premiers_multiples(n):
    print(f"Les 5 premiers multiples de {n} sont :")
    for i in range(1, 6):
        print(f"{n} x {i} = {n * i}")

# Test de la fonction
# nombre = int(input("Entrez un nombre : "))
# cinq_premiers_multiples(nombre)

# 2. Conversiion des minutes en Heures et minutes
def convertir_min_heures_min(min):
    # je suis dans la fonction
    heures = min // 60 # recupérer uniquement la partie entière

    reste_min = min % 60 # recupérer le reste de la division

    print(f"{min} min = {heures} heure(s) et {reste_min} minute(s)")
# je ne suis plus dans la fonction

# Test de la fonction
# min_saisie = int(input("Entrez un nombre de minutes : "))
# convertir_min_heures_min(min_saisie)

# 3. Conversion celsius en Fahrenheit
def celsius_vers_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

# Test de la fonction
celsius_saisie = float(input("Entrez une température en Celsius : "))
celsius_vers_fahrenheit(celsius_saisie)