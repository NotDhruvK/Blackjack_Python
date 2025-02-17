import random

class deck:
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    full_deck = []
    unshuffled_deck = []


    def __init__(self):
        for i in self.suits:
            for j in self.card_values:
                self.full_deck.append(f"{j} of {i}")
        self.unshuffled_deck = self.full_deck


    def restack_deck(self):
        self.full_deck.clear()
        for i in self.suits:
            for j in self.card_values:
                self.full_deck.append(f"{j} of {i}")
        
        self.shuffle_deck(2)


    def shuffle_deck(self, number):
        for i in range(number):
            random.shuffle(self.full_deck)

    
    def deal_card(self):
        top_card = self.full_deck[0]
        self.full_deck.pop(0)
        return top_card