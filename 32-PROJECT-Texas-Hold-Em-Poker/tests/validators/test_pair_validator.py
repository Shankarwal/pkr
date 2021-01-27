import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exactly_one_pair(self):
        cards = [
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_return_pair_from_card_collection(self):
        ten_of_clubs = Card(rank = "10", suit = "Clubs")
        ten_of_spades = Card(rank = "10", suit = "Spades")

        cards = [
            Card(rank = "2", suit= "Diamonds"),
            Card(rank = "5", suit= "Hearts"),
            ten_of_clubs,
            ten_of_spades,
            Card(rank = "Ace", suit= "Clubs")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_clubs,ten_of_spades]
        )