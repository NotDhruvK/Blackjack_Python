import deck_of_cards
import player
import dealer

# Check the Winner
def check_winner(player_total, dealer_total):
    if player_total == dealer_total:
        return "Draw"
    if player_total == 21:
        return "Player"
    if dealer_total == 21:
        return "Dealer"
    if(player_total > 21):
        return "Dealer"
    if (dealer_total > 21):
        return "Player"
    if ((player_total > dealer_total) and (player_total < 22)):
        return "Player"
    if ((player_total < dealer_total) and (dealer_total < 22)):
        return "Dealer" 
    

if __name__ == "__main__":
    # Make and shuffle the deck
    deck = deck_of_cards.deck()
    deck.shuffle_deck(2)

    # Make the players
    Dhruv = player.player("Dhruv")
    Hans = dealer.dealer()

    choice = "start"
    while(choice.lower() != "quit"):
        print("Starting a new game.")
        # Deal the first two cards
        print()
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

        # Game loop
        while(Dhruv.player_In and Hans.player_In):
            print("What do you want to do?")
            choice = input("Hit, Stay, or Double Down?: ")

            if choice.lower() == 'hit':
                card = deck.deal_card()
                Dhruv.hit(card)
                Dhruv.show_cards()
                player_total = Dhruv.total()
                if (player_total > 21):
                    print("You went bust!\nDealer Wins")
                    break
                continue

            elif choice.lower() == "stay":
                Dhruv.set_in_false()
                Hans.show_revealed_cards()
                player_total = Dhruv.total()

                while(Hans.current_total < 16):
                    print("Dealer will take another card")
                    card = deck.deal_card()
                    Hans.hit(card)
                    Hans.current_total = Hans.total()
                    dealer_total = Hans.current_total
                    Hans.show_revealed_cards()
                    # print(Hans.current_total)
                
                winner = check_winner(player_total, dealer_total)
                if winner == "draw":
                    print("It's a draw. You win your bet back.")
                print(f"{winner} wins!!")
                break
            
            elif choice.lower() == "double down":
                if(Dhruv.turn > 2):
                    print("\nYou cannot double down at this point of the game. Please choose hit or stay")
                    continue
                
                card = deck.deal_card()
                Dhruv.hit(card)
                Dhruv.show_cards()
                
                Dhruv.set_in_false()
                Hans.show_revealed_cards()
                player_total = Dhruv.total()

                while(Hans.current_total < 16):
                    print("Dealer will take another card")
                    card = deck.deal_card()
                    Hans.hit(card)
                    Hans.current_total = Hans.total()
                    dealer_total = Hans.current_total
                    Hans.show_revealed_cards()
                
                winner = check_winner(player_total, dealer_total)
                if winner == "draw":
                    print("It's a draw. You win your bet back.")
                print(f"{winner} wins!!")
                break

        choice = input("Would you like to play again?: ").lower()
        while (True):
            if choice == "yes":
                Dhruv.set_in_true()
                Hans.set_in_true()
                choice2 = input("Restack the deck?: ").lower()
                if choice2 == "yes":
                    deck.restack_deck()
                    Dhruv.current_hand = []
                    Hans.current_hand = []
                    Dhruv.current_total = 0
                    Hans.current_total = 0
                    break
                elif choice2 == "no":
                    deck.shuffle_deck(2)
                    Dhruv.current_hand = []
                    Hans.current_hand = []
                    break

            elif choice == "no":
                print(f"Thanks for playing. You won blank ")
                choice = "quit"
                break

            else:
                print("I do not understand that. Please try again.")