class Livre:
    def __init__(self, titre: str=None, auteur: str=None, prix: float=None, annee: int=None) -> None:
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
        self.annee = annee

    def __str__(self):
        return f"{self.titre}\n{self.auteur}\n{self.prix}\n{self.annee}"
    
    def verifier(self, titre_recherche: str) -> bool:
        return self.titre == titre_recherche

if __name__== "__main__":
    livre1 = Livre(titre="Ne tirez pas sur l'oiseau moqueur", auteur="Harper Lee")
    livre2 = Livre(titre="Soufi, mon amour", auteur="Elif Shafak", prix=12.8, annee=2008)

    print(livre1)
    print()
    print(livre2)
    print()
    print(livre2.verifier(titre_recherche="1984"))
