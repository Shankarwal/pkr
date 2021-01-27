import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_clubs = Card(rank = "7", suit = "Clubs")
        self.seven_of_hearts = Card(rank = "7", suit = "Hearts")
        self.seven_of_spades = Card(rank = "7", suit = "Spades")
        self.ten_of_clubs    = Card(rank = "10", suit = "Clubs")
        self.ten_of_diamonds    = Card(rank = "10", suit = "Diamonds")

        self.cards = [
            self.seven_of_clubs,
            self.seven_of_hearts,
            self.seven_of_spades,
            Card(rank = "9", suit = "Clubs"),
            self.ten_of_clubs,
            self.ten_of_diamonds,
            Card(rank = "Queen", suit = "Hearts")
        ]
        
    def test_validates_cards_have_three_of_a_kind_and_two_of_other(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_valid_cards(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven_of_clubs,
                self.seven_of_hearts,
                self.seven_of_spades,
                self.ten_of_clubs,
                self.ten_of_diamonds
            ]
        )
