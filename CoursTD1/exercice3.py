class CompteBancaire:
    def __init__(self, numeroCompte: int, nom: str, solde: float) -> None:
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    
    def versement(self, montant: float):# Cette méthode ne retourne rien donc pas besoin de typer le retour (c'est -> None), elle modifie l'attribu solde
        self.solde += montant

    def retrait(self, montant: float): # Cette méthode ne retourne rien donc pas besoin de typer le retour (c'est -> None), elle modifie l'attribu solde
        if montant > self.solde:
            print("Impossible de retirer de l'argent, solde insuffisant")
        else:
            self.solde -= montant

    def commission(self): # Cette méthode ne retourne rien donc pas besoin de typer le retour (c'est -> None), elle modifie l'attribu solde
        self.solde = self.solde * 0.95

    def afficher(self): # Cette méthode ne retourne rien donc pas besoin de typer le retour (c'est -> None)
        print(f"Numéro de compte : {self.numeroCompte}\nNom : {self.nom}\nSolde : {self.solde}")

if __name__ == "__main__":
    compte1 = CompteBancaire(
        numeroCompte=1234,
        nom="IASchool",
        solde=20100.50
    )
    compte1.afficher()
    print() # ligne vide pour un meilleur affichage
    compte1.retrait(montant=100.5)
    compte1.afficher()
    print()
    compte1.retrait(montant=(compte1.solde+100))
    compte1.afficher()
    print()
    compte1.versement(montant=200)
    compte1.afficher()
    print()
    compte1.commission()
    compte1.afficher()