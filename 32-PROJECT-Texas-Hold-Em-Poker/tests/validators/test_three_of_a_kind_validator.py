import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        eight              = Card(rank = "8", suit = "Diamonds")
        king               = Card(rank = "King", suit = "Clubs")
        self.ace_of_clubs  = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        self.ace_of_spades = Card(rank = "Ace", suit = "Spades")

        self.cards = [
            eight,
            king,
            self.ace_of_clubs,
            self.ace_of_hearts,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_threeo_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.ace_of_clubs,
                self.ace_of_hearts,
                self.ace_of_spades
            ]
        )

