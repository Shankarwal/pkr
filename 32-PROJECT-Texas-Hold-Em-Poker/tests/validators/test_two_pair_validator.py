import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.eight_of_diamonds = Card(rank = "8", suit = "Diamonds")
        self.eight_of_hearts   = Card(rank = "8", suit = "Hearts")
        self.king_of_clubs     = Card(rank = "King", suit = "Clubs")
        self.ace_of_clubs      = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_spades     = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            self.eight_of_diamonds,
            self.eight_of_hearts,
            self.king_of_clubs,
            self.ace_of_clubs,
            self.ace_of_spades
        ]

    def test_validates_cards_have_atleast_two_pair_of_same_rank(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_return_collection_of_cards_that_form_pairs(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.eight_of_diamonds,
                self.eight_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )
