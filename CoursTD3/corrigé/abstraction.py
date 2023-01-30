from abc import ABC, abstractmethod

class BadLength(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class MauvaisNiveau(Exception):
    def __init__(self, message: str="Mauvais niveau renseigné") -> None:
        super().__init__(message)

class Personne(ABC):
    @abstractmethod
    def walk():
        print('Is walking...')

class Etudiant(Personne):
    niveau = "M2"
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    def walk(self):
        print("Je marche")
    
    @classmethod
    def modifier_niveau(cls, n_niveau: str):
        if len(n_niveau) > 2:
            raise BadLength("Trop élevé")
        if (n_niveau != "M1") and (n_niveau != "M2"):
            raise MauvaisNiveau()
        cls.niveau = n_niveau

    @staticmethod
    def est_de_niveau_M2(niveau):
        return niveau == "M2"

if __name__ == "__main__":
    etu = Etudiant(name="Imène")
    print(etu)
    print(etu.__dict__)
    etu.walk()

    print(Etudiant.niveau)
    try: 
        Etudiant.modifier_niveau(n_niveau="M1")
    except MauvaisNiveau as e:
        print(type(e))
        print("Les niveaux acceptés ne sont que M1 et M2")
        print(e)
    except BadLength as e:
        print(type(e))
        print("Le nivau ne peut pas avoir plus de 2 caractères")
        print(e)
    finally:
        print("L'execution continue")

    print(Etudiant.niveau)

    print(Etudiant.est_de_niveau_M2(niveau="M1"))

    a, b = 9, 10
    print(a & b)
    print(a and b)

    a, b = True, False
    print(a & b)
    print(a and b)
