# ======================
# TP1 - Exercice 3
# ======================
# Inverse d'une chaîne
def inverseChaine(ch):
    inverse = ""

    # debut de la boucle
    for i in range(len(ch) - 1, -1, -1):
        inverse += ch[i]
    # fin de la boucle
    
    # retourner le chaine
    return inverse

chaine = input("Saisissez la chaîne : ")
print(f"L'inverse de la chaîne {chaine} est : {inverseChaine(chaine)}")

# Vérifier si une chaîne est un Palindrome
def estPalindrome(ch):
    if ch == inverseChaine(ch):
        print(f"La chaîne {ch} est un palindrome")
    else:
        print(f"La chaîne {ch} n'est pas un palindrome")

# test de palindrome
estPalindrome(chaine)


# Bonus
def inverseChaineWhile(ch):
    inverse = ""
    i = len(ch) - 1        # Commence à la finb de la chaine
    while i >= 0:          # Condition d'arrêt
        inverse += ch[i]
        i -= 1             # Décrémentation
    
    # retourner la chaine inversée
    return inverse

# test
print(f"L'inverse de la chaine {chaine} avec la boucle while est : {inverseChaineWhile(chaine)}")

def inverseChainePro(ch):
    return ch[::-1]

# test
print(f"L'inverse de la chaine {chaine} avec la méthode [::-1] est : {inverseChainePro(chaine)}")