# Déclaration de variables
nom = "TCHEROU"
prenom = "Maliki"
message: str = "Bonjour tout le monde"
char: chr = 'M' # déclaration d'un caractère typé
age = 34
a: int = 60
pi: float = 3.14
est_vrai: bool = True
tableau = [1, 2, 3, 4, 5]
tableauA: list = [1, 2, 3, 4, 5]
objet = {"nom": "TCHEROU", "prenom": "Maliki"}
objetT: object = {"nom": "TCHEROU", "prenom": "Maliki"}

# Affichage des variables
print("Nom :", nom)
print("Prénom :", prenom)

# Déclaration d'unne fonction
# Fonction non typée
def somme1(a, b):
    return a + b

# Fonction typée
def somme2(a: int, b: int) -> int:
    return a + b

# Test des fonctions
res1 = somme1(34, 12)
print("Résultat de somme1 :", res1)

print("Résultat de somme2 :", somme2(34, 12))

## Les boucles
# tableau = [1, 2, 3, 4, 5]
def boucleFor1(t):
    print("***** boucleFor1 *****")
    for i in range(0, len(t), 1):
        print(t[i])

# test de la boucle boucleFor1
boucleFor1(tableau)

def boucleFor2(t):
    print("***** boucleFor2 *****")
    for i in range(len(t)):
        print(t[i])

# test de la boucle boucleFor2
boucleFor2(tableau)

def boucleFor3(t):
    print("***** boucleFor3 *****")
    [print(t[i]) for i in range(len(t))]

# test de la boucle boucleFor3
boucleFor3(tableau)

def boucleWhile(t):
    print("***** Boucle while *****")
    i = 0               # initialisation
    while i < len(t):   # condition d'arrêt
        print(t[i])
        # i = i + 1
        i += 1          # incrémentation

# test de la boucle while
boucleWhile(tableau)