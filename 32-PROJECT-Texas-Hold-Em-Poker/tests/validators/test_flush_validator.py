import unittest

from poker.card import Card
from poker.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_hearts = Card(rank = "2", suit = "Hearts")
        self.six_of_hearts = Card(rank = "6", suit = "Hearts")
        self.seven_of_hearts = Card(rank = "7", suit = "Hearts")
        self.nine_of_hearts = Card(rank = "9", suit = "Hearts")
        self.jack_of_hearts = Card(rank = "Jack", suit = "Hearts")
        self.ace_of_hearts = Card(rank = "Ace", suit = "Hearts")

        self.cards = [
            self.two_of_hearts,
            self.six_of_hearts,
            self.seven_of_hearts,
            self.nine_of_hearts,
            self.jack_of_hearts,
            Card(rank = "Queen", suit = "Clubs"),
            self.ace_of_hearts
        ]

    def test_validates_five_cards_of_same_suit_exist_in_collection(self):
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_five_highest_cards_with_same_suit(self):
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.six_of_hearts,
                self.seven_of_hearts,
                self.nine_of_hearts,
                self.jack_of_hearts,
                self.ace_of_hearts
            ]
        )