from game import Game
from player import Player
from dealer import Dealer
from deck import Deck


def blackjack(game, player, dealer, deck):
    while True:
        if len(deck.deck) < 4:
            print("Deck empty, reshuffling...")
            deck.shuffle()
        print("Dealing cards...")
        dealer.deal(deck, player)
        print(f"Dealer shows {dealer.hand[0].full_name}.")
        print(f"Your cards are:")
        for card in player.hand:
            print(f"{card.full_name}")
        while True:
            action = input("(H)it or (S)tand? ")
            action = action.lower()
            if action == 'h':
                deck.draw(player.hand)
                print(f"You drew the {player.hand[-1].full_name}.")
            else:
                break
        print("You stand. Dealer is drawing...")
        draws = dealer.draw_up(deck)
        print(f"Dealer draws {draws} {'card' if draws == 1 else 'cards'}.")
        print("Dealer reveals cards:")
        for card in dealer.hand:
            print(f"{card.full_name}")
        dealer_score = game.get_hand_score(dealer.hand)
        player_score = game.get_hand_score(player.hand)
        print(f"Dealer has {dealer_score} points.")
        print(f"You have {player_score} points.")
        winner, score = game.get_winner(dealer, player)
        if winner == dealer and score == -1:
            print("You busted! The dealer wins.")
        elif winner == player:
            print(f"You win by {score} {'point' if score == 1 else 'points'}!")
        elif winner == dealer:
            print(f"The dealer wins by {score} {'point' if score == 1 else 'points'}!")
        else:
            print(f"You tied at {player_score} points.")
        print(f"You have won {player.wins} {'time' if player.wins == 1 else 'times'}.")
        print(f"The dealer has won {dealer.wins} {'time' if dealer.wins == 1 else 'times'}.")
        keep_playing = input("Would you like to continue playing (y/n)? ")
        if keep_playing.lower() == 'n':
            break
        else:
            print("Returning cards...")
            dealer.return_cards(deck, player)


def main():
    # Initialize game and make player
    game = Game()
    p_name = input("Enter player name (enter for default): ")
    player = Player(p_name)
    dealer = Dealer()
    deck = Deck()
    deck.shuffle()
    # Main program loop
    blackjack(game, player, dealer, deck)


if __name__ == "__main__":
    main()
