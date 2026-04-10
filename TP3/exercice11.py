class CompteBancaire:
    def __init__(self, titulaire, solde):
        # attribut titulaire est public (directement accessible)
        self.titulaire = titulaire

        # attribut solde est privé (accessible uniquement à l'intérieur de la classe)
        self.__solde = solde

    # ================
    # Méthodes d'accès (getters)
    # ================
    def get_solde(self):
        return self.__solde

    # ================
    # Méthodes de modification (setters)
    # ================
    def set_solde(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide.")

    # ================
    # Méthodes métier
    # ================
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"{montant} MAD déposés")
        else:
            print("Montant de dépôt invalide.")

    def retirer(self, montant):
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            print(f"{montant} MAD retirés")
        else:
            print("Montant de retrait invalide ou solde insuffisant.")

    def afficher_solde(self):
        print(f"Solde actuel: {self.__solde} MAD")

## Phase de test
def test_compte():
    compte = CompteBancaire("Alice", 1000)

    # Test des dépôts
    compte.deposer(500)
    compte.afficher_solde()

    compte.deposer(-200)
    compte.afficher_solde()

    # Test des retraits
    compte.retirer(300)
    compte.afficher_solde()

    compte.retirer(1500)
    compte.afficher_solde()

test_compte()
