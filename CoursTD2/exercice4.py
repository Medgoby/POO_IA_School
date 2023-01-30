from __future__ import annotations


class DeadPokemonError(Exception):
    """Exception à lever quand le Pokemon est mort"""
    def __init__(self, message: str="Dead Pokemon, attack another one.") -> None:
        super().__init__(message)

class Pokemon:
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        self._nom = nom
        self._hp = hp
        self._atk = atk

    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, value: float):
        self._nom = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value: float):
        self._hp = value
    
    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, value: float):
        self._atk = value

    def is_dead(self) -> bool:
        """Retourne True si le Pokémon est mort, False sinon."""
        return self._hp == 0

    @staticmethod
    def _reduire_hp(hp: float, atk: float) -> float:
        """
        Méthode statique protégée qui n'est utilisée que par la classe elle-même et ses classes filles
        La méthode est statique car elle n'utilise pas les attributs de la classe
        Retourne le hp après lui avoir réduit un certain nombre d'atk
        """
        if hp > atk:
            hp -= atk
        else :
            hp = 0
        return hp

    def attaquer(self, p: Pokemon):
        """
        Méthode attaquer(), utilise la méthode _reduire_hp()
        Modifie l'attribut hp du Pokémon p donné en entrée, et donc ne retourne rien
        """
        if p.is_dead():
            raise DeadPokemonError()
        p.hp = self._reduire_hp(hp=p.hp, atk=self._atk)
    
    def __str__(self) -> str:
        return f"{self._nom}, HP: {self._hp}, ATK: {self._atk}, TYPE: {self.__class__.__name__}"

class PokemonFeu(Pokemon):
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        super().__init__(nom, hp, atk)

    def attaquer(self, p: Pokemon):
        if p.is_dead():
            raise DeadPokemonError() # Si le pokemon est mort alors lever une exception
        if isinstance(p, PokemonPlante): # Si le Pokémon p est de type PokemonPlante alors l'attaque est double
            p.hp = super()._reduire_hp(hp=p.hp, atk=(2 * self._atk))
        elif isinstance(p, (PokemonEau, PokemonPlante)):  # Si le Pokémon p est de type PokemonFeu ou PokemonEau alors l'attaque est divisée par 2
             p.hp = super()._reduire_hp(hp=p.hp, atk=(0.5 * self._atk))
        else: # Sinon si le Pokémon p est de type Pokemon seulement alors l'attaque est régulière
            super().attaquer(p=p)

class PokemonEau(Pokemon):
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        super().__init__(nom, hp, atk)
    
    def attaquer(self, p: Pokemon):
        if p.is_dead():
            raise DeadPokemonError()
        if isinstance(p, PokemonFeu):
             p.hp = super()._reduire_hp(hp=p.hp, atk=(2 * self._atk))
        elif isinstance(p, (PokemonFeu, PokemonPlante)):
             p.hp = super()._reduire_hp(hp=p.hp, atk=(0.5 * self._atk))
        else:
            super().attaquer(p=p)

class PokemonPlante(Pokemon):
    def __init__(self, nom: str, hp: float, atk: float) -> None:
        super().__init__(nom, hp, atk)

    def attaquer(self, p: Pokemon):
        if p.is_dead():
            raise DeadPokemonError()
        if isinstance(p, PokemonFeu):
             p.hp = super()._reduire_hp(hp=p.hp, atk=(2 * self._atk))
        elif isinstance(p, (PokemonFeu, PokemonEau)):
             p.hp = super()._reduire_hp(hp=p.hp, atk=(0.5 * self._atk))
        else:
            super().attaquer(p=p)

if __name__ == "__main__":
    print("***** Créer les Pokemons *****\n")
    p = Pokemon(nom="Germignon", hp=100, atk=10)
    print(p)
    p_eau = PokemonEau(nom="Carapuce", hp=100, atk=20)
    print(p_eau)
    p_feu = PokemonFeu(nom="Salamèche", hp=100, atk=20)
    print(p_feu)
    p_plante = PokemonPlante(nom="Germignon", hp=100, atk=20)
    print(p_plante) 

    print("\n***** Commencer le combat *****\\n")
    try:
        print("\nPokemonEau attaque Pokemon")
        p_eau.attaquer(p=p)
        print(p)
    except DeadPokemonError as e:
        print(p)
        print(e)

    try:
        print("PokemonFeu attaque PokemonEau")
        p_feu.attaquer(p_eau)
        print(p_eau)
    except DeadPokemonError as e:
        print(p_feu)
        print(e)
    
    try:
        print("\nPokemonPlante attaque PokemonEau")
        p_plante.attaquer(p_feu)
        print(p_feu)
        print("\nPokemonPlante attaque PokemonEau")
        p_plante.attaquer(p_feu)
        print(p_feu)
        print("\nPokemonPlante attaque PokemonEau")
        p_plante.attaquer(p_feu)
        print(p_feu)
    except DeadPokemonError as e:
        print(p_feu)
        print(e)
    
    # le Pokemon p_feu a un HP, testons alors l'attaque
    # Elle devrait retourner un message d'exception (clause except)
    try:
        print("\nPokemonPlante attaque PokemonEau")
        p_plante.attaquer(p_feu)
        print(p_feu)
    except DeadPokemonError as e:
        print(p_feu)
        print(e.__class__)
        print(e)
