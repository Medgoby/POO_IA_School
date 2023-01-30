# Card Game

# Shapes: clubs (trèfle), diamonds (carré), hearts (coeur), spades (pique)
# Values : Ace, 2-9, King, Queen, Jack

from random import shuffle

class Card():
    def __init__(self, value, shape) -> None:
        self.value = value
        self.shape = shape
    
    def card_name(self):
        return f"{self.value} of {self.shape}"

class CardGame():
    def __init__(self) -> None:
        shapes = ["Club", "Diamond", "Heart", "Spade"]
        values = ["Ace", *[str(elem) for elem in range(2, 11)] , "King", "Queen", "Jack"]

        self.cards = []
        for shape in shapes:
            for value in values:
                self.cards.append(Card(value=value, shape=shape))

    def suffle_cards(self):
        shuffle(self.cards) 

    def extract_card(self) -> Card:
        if len(self.cards) == 0:
            print("No more cards to extract")
            return None
        else:
            extracted_card = self.cards[0]
            self.cards = self.cards[1:]
            return extracted_card

    def show_cards(self):
        for card in self.cards:
            print(card.card_name())


if __name__ == "__main__":
    print("**************Card game**************")
    print("Create card game")
    g = CardGame()
    g.show_cards()

    print("Shuffle card game")
    g.suffle_cards()
    g.show_cards()

    print("Extract all cards of game")
    for i in range(52):
        print(f"Extracted card: {g.extract_card().card_name()}")