class player():
    def __init__(self, name):
        self.turn = 0
        self.name = name
        self.current_hand =  []
        self.current_total = 0
        pass

    def hit(self, card):
        self.turn += 1
        self.current_hand.append(card)

    def double_down(self):
        pass

    def split_cards(self):
        pass

    def show_cards(self):
        print("Your Cards are: ")
        for card in self.current_hand:
            print(card)
        print("\n")

    def total(self):
        for card in self.current_hand:
            print(card[0])
            denomination = card[0]
            if denomination == '2':
                self.current_total += 2
            if denomination == '3':
                self.current_total += 3
            if denomination == '4':
                self.current_total += 4
            if denomination == '5':
                self.current_total += 5
            if denomination == '6':
                self.current_total += 6
            if denomination == '7':
                self.current_total += 7
            if denomination == '8':
                self.current_total += 8
            if denomination == '9':
                self.current_total += 9
            if denomination == '1':
                self.current_total += 10
            if denomination == 'J' or denomination == 'Q' or denomination == 'K':
                self.current_total += 10
            if denomination == 'A':
                if self.current_total < 11:
                    self.current_total += 11
                else:
                    self.current_total += 1

        return self.current_total