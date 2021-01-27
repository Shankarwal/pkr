import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_validates_there_are_no_five_consecutive_cards_of_same_suit(self):
        cards = [
            Card(rank = "6", suit = "Diamonds"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "8", suit = "Diamonds"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "10", suit = "Clubs"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_there_are_five_consecutive_cards_of_same_suit(self):
        cards = [
            Card(rank = "6", suit = "Diamonds"),
            Card(rank = "7", suit = "Diamonds"),
            Card(rank = "8", suit = "Diamonds"),
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "10", suit = "Diamonds"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_validates_there_are_five_consecutive_cards_of_same_suit(self):
        six   = Card(rank = "6", suit = "Diamonds")
        seven = Card(rank = "7", suit = "Diamonds")
        eight = Card(rank = "8", suit = "Diamonds")
        nine  = Card(rank = "9", suit = "Diamonds")
        ten   = Card(rank = "10", suit = "Diamonds")

        cards = [
            six,
            seven,
            eight,
            nine,
            ten,
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                six,
                seven,
                eight,
                nine,
                ten
            ]
        )