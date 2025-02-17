class dealer():
    def __init__(self):
        self.current_hand =  []
        self.current_total = 0
        self.player_In = True
        pass

    def hit(self, card):
        self.current_hand.append(card)

    def show_cards(self):
        print("Dealer's cards are: ")
        for i, card in enumerate(self.current_hand):
            if i == 0:
                print("Hidden Card")
            else:
                print(card)
        print("\n")

    def show_revealed_cards(self):
        print("\nDealer's final cards are: ")
        for card in self.current_hand:
            print(card)
        print("\n")

    def set_in(self):
        self.player_In = not (self.player_In)

    def total(self):
        self.current_total = 0
        for card in self.current_hand:
            denomination = card[0:1]
            if denomination == '2 ':
                self.current_total += 2
            if denomination == '3 ':
                self.current_total += 3
            if denomination == '4 ':
                self.current_total += 4
            if denomination == '5 ':
                self.current_total += 5
            if denomination == '6 ':
                self.current_total += 6
            if denomination == '7 ':
                self.current_total += 7
            if denomination == '8 ':
                self.current_total += 8
            if denomination == '9 ':
                self.current_total += 9
            if denomination == '10':
                self.current_total += 10
            if denomination == 'J ' or denomination == 'Q ' or denomination == 'K ':
                self.current_total += 10
            if denomination == 'A ':
                if self.current_total < 11:
                    self.current_total += 11
                else:
                    self.current_total += 1
        
        return self.current_total