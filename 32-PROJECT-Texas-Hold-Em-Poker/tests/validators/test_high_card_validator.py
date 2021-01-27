import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card(rank = "Jack", suit = "Spades"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_return_high_card_from_card_collection(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")

        cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "5", suit = "Clubs"),
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "10", suit = "Diamonds"),
            ace_of_spades
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_spades]
        )