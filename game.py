class Game:
    @staticmethod
    def get_hand_score(hand):
        total = 0
        aces = 0
        for card in hand:
            value = card.get_value()
            if value == 11:
                aces += 1
            total += value
        while aces > 0 and total > 21:
            total -= 10
            aces -= 1
        return total

    def get_winner(self, dealer, player):
        dealer_score = self.get_hand_score(dealer.hand)
        player_score = self.get_hand_score(player.hand)
        if player_score > 21:
            dealer.wins += 1
            return dealer, -1
        if dealer_score > player_score:
            dealer.wins += 1
            return dealer, dealer_score - player_score
        elif dealer_score < player_score:
            player.wins += 1
            return player, player_score - dealer_score
        else:
            return None, 0
