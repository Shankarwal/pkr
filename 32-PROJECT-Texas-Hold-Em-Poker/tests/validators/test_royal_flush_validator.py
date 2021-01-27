import unittest

from poker.card import Card
from poker.validators import RoyalFlushValdator

class RoyalFlushValdatorTest(unittest.TestCase):
    def test_validates_cards_do_not_have_a_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "9", suit = "Diamonds"),
            Card(rank = "10", suit = "Diamonds"),
            Card(rank = "Jack", suit = "Diamonds"),
            Card(rank = "Queen", suit = "Diamonds"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = RoyalFlushValdator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_cards_do_have_a_straight_flush_ending_in_ace(self):
        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Diamonds"),
            Card(rank = "Jack", suit = "Diamonds"),
            Card(rank = "Queen", suit = "Diamonds"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = RoyalFlushValdator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_cards_with_rank_ending_in_ace(self):
        ten   = Card(rank = "10", suit = "Diamonds")
        jack  = Card(rank = "Jack", suit = "Diamonds")
        queen = Card(rank = "Queen", suit = "Diamonds")
        king  = Card(rank = "King", suit = "Diamonds")
        ace   = Card(rank = "Ace", suit = "Diamonds")

        cards = [
            Card(rank = "2", suit = "Spades"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = RoyalFlushValdator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten,
                jack,
                queen,
                king,
                ace
            ]
        )