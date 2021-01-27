import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_clubs    = Card(rank = "7", suit = "Clubs")
        self.seven_of_diamonds = Card(rank = "7", suit = "Diamonds")
        self.seven_of_hearts   = Card(rank = "7", suit = "Hearts")
        self.seven_of_spades   = Card(rank = "7", suit = "Spades")

        self.cards = [
            Card(rank = "4", suit = "Diamonds"),
            self.seven_of_clubs,
            self.seven_of_diamonds,
            self.seven_of_hearts,
            self.seven_of_spades,
            Card(rank = "9", suit = "Clubs"),
            Card(rank = "King", suit = "Diamonds")
        ]

    def test_validates_there_are_four_cards_of_same_rank(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_valid_cards(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_clubs,
                self.seven_of_diamonds,
                self.seven_of_hearts,
                self.seven_of_spades,
            ]
        )
