class Animal:
    def parler(self):
        print("L'animal fait du bruit")

class Chien(Animal):
    def parler(self):
        print("Le chien aboie")

class Chat(Animal):
    def parler(self):
        print("Le chat miaule")

# Phase de test
a1 = Chien()
a1.parler()

a2 = Chat()
a2.parler()

