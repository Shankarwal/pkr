import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        two        = Card(rank = "2", suit = "Clubs")
        six        = Card(rank = "6", suit = "Spades")
        self.seven = Card(rank = "7", suit = "Clubs")
        self.eight = Card(rank = "8", suit = "Hearts")
        self.nine  = Card(rank = "9", suit = "Clubs")
        self.ten   = Card(rank = "10", suit = "Diamonds")
        self.jack  = Card(rank = "Jack", suit = "Spades")

        self.cards = [
            two,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_figures_out_straight_is_best_rank(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Hearts")
        ]

        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack 
            ]
        )