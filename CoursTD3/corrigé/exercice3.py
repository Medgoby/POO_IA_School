from abc import ABC, abstractclassmethod, abstractmethod
from typing import List

class TableauTrieAbstrait(ABC):
    @abstractmethod
    def plus_grand(self, a, b):
        pass

    @abstractmethod
    def inserer(self, element):
        pass

    @abstractclassmethod
    def modifier_taille_max():
        pass

class TableauTrieEntiers(TableauTrieAbstrait):
    TAILLE_MAX: int = 5
    def __init__(self) -> None:
        self.tableau: List[int] = []

    def __str__(self) -> str:
        return f"{self.tableau}"

    def plus_grand(self, a: int, b: int):
        return a > b
    
    def inserer(self, element: int) -> None:
        if len(self.tableau) >= self.TAILLE_MAX:
            raise Exception(f"Taille actuelle du tableau insufisante = {self.TAILLE_MAX}.\nAugmenter la taille du tableau pour y insérer plus d'éléments.")
        if (len(self.tableau) == 0):
            self.tableau.insert(0, element)
            return
        elif (self.plus_grand(a=element, b=max(self.tableau))):
            self.tableau.insert(len(self.tableau), element)
            return
        for i in range(len(self.tableau)):
            if (self.plus_grand(a=self.tableau[i], b=element))\
                | (self.tableau[i] == element):
                self.tableau.insert(i, element)
                return
    
    @classmethod
    def modifier_taille_max(cls, nouvelle_taille_max: int):
        cls.TAILLE_MAX = nouvelle_taille_max

class TableauTrieChaines(TableauTrieAbstrait):
    TAILLE_MAX: int = 5
    def __init__(self) -> None:
        self.tableau: List[str] = []
    
    def __str__(self) -> str:
        return f"{self.tableau}"

    def plus_grand(self, a: str, b: str):
        return len(a) > len(b)

    def inserer(self, element: int) -> None:
        if len(self.tableau) >= self.TAILLE_MAX:
            raise Exception(f"Taille actuelle du tableau insufisante = {self.TAILLE_MAX}.\nAugmenter la taille du tableau pour y insérer plus d'éléments.")
        if (len(self.tableau) == 0):
            self.tableau.insert(0, element)
            return
        elif (self.plus_grand(a=element, b=max(self.tableau))):
            self.tableau.insert(len(self.tableau), element)
            return
        for i in range(len(self.tableau)):
            if (self.tableau[i] == element):
                raise Exception("Element already exists in list")
            if (self.plus_grand(a=self.tableau[i], b=element)):
                self.tableau.insert(i, element)
                return
    
    @classmethod
    def modifier_taille_max(cls, nouvelle_taille_max: int):
        cls.TAILLE_MAX = nouvelle_taille_max

if __name__ == "__main__":
    print("Tableau d'entiers :")
    tableau_entiers = TableauTrieEntiers()
    tableau_entiers.inserer(element=2)
    print(tableau_entiers)
    tableau_entiers.inserer(element=3)
    print(tableau_entiers)
    tableau_entiers.inserer(element=1)
    print(tableau_entiers)
    tableau_entiers.inserer(element=5)
    print(tableau_entiers)
    tableau_entiers.inserer(element=4)
    print(tableau_entiers)
    try:
        tableau_entiers.inserer(element=6)
        print(tableau_entiers)
    except Exception as e:
        print(e)

    print("\nTableau de chaines :")
    tableau_chaines = TableauTrieChaines()
    tableau_chaines.inserer("Hello")
    print(tableau_chaines)
    tableau_chaines.inserer("Hello there !")
    print(tableau_chaines)
    tableau_chaines.inserer("Oh")
    print(tableau_chaines)
    try:
        tableau_chaines.inserer("Oh")
        print(tableau_chaines)
    except Exception as e:
        print(e)

    # A vous de proposer des optimisations et une meilleure conception si possible
    