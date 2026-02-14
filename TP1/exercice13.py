# ======================
# TP1 - Exercice 13
# ======================

# Trouvons les N premiers termes de Fibonacci
def fibonacci(n):
    a = 0
    b = 1

    if n >= 1:
        print(a, end=" ")
    
    if n >= 2:
        print(b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        # a = b
        # b = c
        a, b = b, c

# Phase de test
print("====== Suite de Fibonacci ======")
nombre = int(input("Entrez le nombre de termes à afficher : "))
fibonacci(nombre)
