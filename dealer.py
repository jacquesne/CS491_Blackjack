from game import Game


class Dealer:
    def __init__(self):
        self.wins = 0
        self.hand = []

    def deal(self, deck, player):
        deck.draw(self.hand, 2)
        deck.draw(player.hand, 2)

    def return_cards(self, deck, player):
        for card in self.hand:
            deck.return_card(card)
        self.hand.clear()
        for card in player.hand:
            deck.return_card(card)
        player.hand.clear()

    def draw_up(self, deck):
        draws = 0
        while Game.get_hand_score(self.hand) < 17:
            deck.draw(self.hand)
            draws += 1
        return draws
