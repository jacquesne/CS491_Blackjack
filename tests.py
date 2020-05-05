import unittest
import deck
import game
import dealer
import player


class TestCard(unittest.TestCase):
    def test_card_get_value_ace(self):
        card = deck.Card(1, 0)
        value = card.get_value()
        self.assertEqual(value, 11)

    def test_card_get_value_queen(self):
        card = deck.Card(12, 0)
        value = card.get_value()
        self.assertEqual(value, 10)

    def test_card_get_value_too_large(self):
        card = deck.Card(14, 0)
        value = card.get_value()
        self.assertIsNone(value)

    def test_card_get_name_queen(self):
        name = deck.Card.get_name(12)
        self.assertEqual(name, "Queen")

    def test_card_get_name_too_large(self):
        name = deck.Card.get_name(14)
        self.assertIsNone(name)


class TestDeck(unittest.TestCase):
    def test_generate_deck_first(self):
        card_deck = deck.Deck.generate_decks(1)
        self.assertEqual(card_deck[0].name, "Ace")

    def test_generate_deck_length(self):
        card_deck = deck.Deck.generate_decks(1)
        self.assertEqual(len(card_deck), 52)

    def test_shuffle_order(self):
        new_deck = deck.Deck()
        original = new_deck.deck.copy()
        new_deck.shuffle()
        self.assertNotEqual(original, new_deck)

    def test_draw_first(self):
        new_deck = deck.Deck()
        card = new_deck.draw_one()
        self.assertEqual(card.name, "Ace")

    def test_draw_empty(self):
        new_deck = deck.Deck()
        new_deck.deck.clear()
        card = new_deck.draw_one()
        self.assertIsNone(card)

    def test_return_card_one(self):
        new_deck = deck.Deck()
        card = new_deck.draw_one()
        new_deck.return_card(card)
        self.assertEqual(new_deck.discarded[0].name, "Ace")


class TestGame(unittest.TestCase):
    def test_get_hand_score_no_aces(self):
        hand = [deck.Card(5, 0), deck.Card(12, 0)]
        score = game.Game.get_hand_score(hand)
        self.assertEqual(score, 15)

    def test_get_hand_score_with_ace_low(self):
        hand = [deck.Card(5, 0), deck.Card(1, 0)]
        score = game.Game.get_hand_score(hand)
        self.assertEqual(score, 16)

    def test_get_hand_score_with_ace_high(self):
        hand = [deck.Card(5, 0), deck.Card(13, 0), deck.Card(1, 0)]
        score = game.Game.get_hand_score(hand)
        self.assertEqual(score, 16)

    def test_get_hand_score_over(self):
        hand = [deck.Card(5, 0), deck.Card(13, 0), deck.Card(9, 1)]
        score = game.Game.get_hand_score(hand)
        self.assertEqual(score, 24)

    def test_get_winner_dealer(self):
        test_dealer = dealer.Dealer()
        test_player = player.Player()
        test_dealer.hand = [deck.Card(5, 0)]
        test_player.hand = [deck.Card(4, 0)]
        test_game = game.Game()
        winner, score = test_game.get_winner(test_dealer, test_player)
        self.assertEqual(winner, test_dealer)

    def test_get_winner_player(self):
        test_dealer = dealer.Dealer()
        test_player = player.Player()
        test_dealer.hand = [deck.Card(4, 0)]
        test_player.hand = [deck.Card(5, 0)]
        test_game = game.Game()
        winner, score = test_game.get_winner(test_dealer, test_player)
        self.assertEqual(winner, test_player)

    def test_get_winner_tie(self):
        test_dealer = dealer.Dealer()
        test_player = player.Player()
        test_dealer.hand = [deck.Card(5, 0)]
        test_player.hand = [deck.Card(5, 0)]
        test_game = game.Game()
        winner, score = test_game.get_winner(test_dealer, test_player)
        self.assertIsNone(winner)

    def test_get_winner_score(self):
        test_dealer = dealer.Dealer()
        test_player = player.Player()
        test_dealer.hand = [deck.Card(8, 0)]
        test_player.hand = [deck.Card(4, 0)]
        test_game = game.Game()
        winner, score = test_game.get_winner(test_dealer, test_player)
        self.assertEqual(score, 4)

    def test_get_winner_bust(self):
        test_dealer = dealer.Dealer()
        test_player = player.Player()
        test_dealer.hand = [deck.Card(8, 0)]
        test_player.hand = [deck.Card(10, 0), deck.Card(10, 0), deck.Card(10, 0)]
        test_game = game.Game()
        winner, score = test_game.get_winner(test_dealer, test_player)
        self.assertEqual(score, -1)


class TestDealer(unittest.TestCase):
    def test_deal(self):
        test_deck = deck.Deck()
        deal = dealer.Dealer()
        play = player.Player()
        deal.deal(test_deck, play)
        self.assertEqual(len(play.hand), 2)

    def test_return_cards(self):
        test_deck = deck.Deck()
        deal = dealer.Dealer()
        play = player.Player()
        deal.deal(test_deck, play)
        deal.return_cards(test_deck, play)
        self.assertEqual(len(test_deck.discarded), 4)

    def test_draw_up_low(self):
        test_deck = deck.Deck()
        deal = dealer.Dealer()
        deal.hand = [deck.Card(10, 0), deck.Card(6, 0)]
        deal.draw_up(test_deck)
        self.assertEqual(len(deal.hand), 3)

    def test_draw_up_high(self):
        test_deck = deck.Deck()
        deal = dealer.Dealer()
        deal.hand = [deck.Card(10, 0), deck.Card(7, 0)]
        deal.draw_up(test_deck)
        self.assertEqual(len(deal.hand), 2)


if __name__ == "__main__":
    unittest.main()
