import random


class Card:
    def __init__(self, base, suit):
        self.base = base
        self.suit = self.get_suit_name(suit)
        self.value = self.get_value()
        self.name = self.get_name(base)

    def get_value(self):
        if self.base == 1:
            return 11
        elif 1 < self.base < 10:
            return self.base
        elif 10 <= self.base <= 13:
            return 10
        else:
            return None

    @staticmethod
    def get_name(base):
        card_names = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        return card_names[base] if 1 <= base <= 13 else None

    @staticmethod
    def get_suit_name(suit):
        suits = {
            1: "Hearts",
            2: "Diamonds",
            3: "Clubs",
            4: "Spades"
        }
        return suits[suit] if 1 <= suit <= 4 else None

    @property
    def full_name(self):
        return f"{self.name} of {self.suit}"


class Deck:
    def __init__(self, num_decks=1):
        self.deck = self.generate_decks(num_decks)
        self.discarded = []

    @staticmethod
    def generate_decks(num_decks):
        deck = []
        for num in range(num_decks):
            for card in range(1, 14):
                for suit in range(1, 5):
                    deck.append(Card(card, suit))
        return deck

    def shuffle(self):
        self.deck.extend(self.discarded)
        self.discarded.clear()
        random.shuffle(self.deck)

    def draw_one(self):
        return self.deck.pop(0) if len(self.deck) > 0 else None

    def return_card(self, card):
        self.discarded.append(card)

    def draw(self, hand, num=1):
        for i in range(num):
            hand.append(self.draw_one())

    def discard(self, hand, card):
        self.return_card(card)
        hand.remove(card)

    def discard_all(self, hand):
        cards = hand.copy()
        for card in cards:
            self.discard(hand, card)
