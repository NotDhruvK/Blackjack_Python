import deck_of_cards
import player
import dealer

# Check the Winner
def check_winner(player_total, dealer_total):
    if(player_total > 21):
        return "Dealer"
    
    if (dealer_total > 21):
        return "Player"
    
    if ((player_total > dealer_total) and (player_total < 22) and (dealer_total > 16)):
        return "Player"

    if ((player_total < dealer_total) and (dealer_total < 22) and (dealer_total > 16)):
        return "Dealer" 
    

if __name__ == "__main__":
    # Make and shuffle the deck
    deck = deck_of_cards.deck()
    deck.shuffle_deck(2)

    # Make the players
    Dhruv = player.player("Dhruv")
    Hans = dealer.dealer()

    # Deal the first two cards
    card = deck.deal_card()
    Dhruv.hit(card)
    card = deck.deal_card()
    Hans.hit(card)
    card = deck.deal_card()
    Dhruv.hit(card)
    card = deck.deal_card()
    Hans.hit(card)

    Dhruv.show_cards()
    Hans.show_cards()
    player_total = Dhruv.total()
    dealer_total = Hans.total()
    
    while(True):
        winner = check_winner(player_total, dealer_total)
        if winner != None:
            print(f"{winner} wins!!")
            print(Dhruv.current_total)
            print(Hans.current_total)
            break

        print("What do you want to do?")
        choice = input("Hit or Stay?: ")

        if choice.lower() == 'hit':
            card = deck.deal_card()
            Dhruv.hit(card)
            Dhruv.show_cards()
            Hans.show_revealed_cards()
            print(Dhruv.current_total)
            print(Hans.current_total)

        elif choice.lower() == "stay":
            Hans.show_revealed_cards()
            winner = check_winner(player_total, dealer_total)
            print(f"{winner} wins!!")
            break
        
        Dhruv.current_total = 0
        Hans.current_total = 0
        player_total = Dhruv.total()
        dealer_total = Hans.total()