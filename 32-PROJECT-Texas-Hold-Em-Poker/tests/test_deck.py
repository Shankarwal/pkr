import unittest
from unittest.mock import patch

from poker.card import Card
from poker.deck import Deck

class DeckTest(unittest.TestCase):
    def test_has_length_that_is_equal_to_count_of_cards(self):
        deck = Deck()
        self.assertEqual(
            len(deck),
            0
        )
        
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_adds_cards_to_its_collections(self):
        card = Card(rank = "Ace", suit = "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )

    @patch("random.shuffle")
    def test_shuffles_cards_in_random_order(seld, mock_shuffle):
        deck = Deck()

        cards = [
            Card(rank = "4", suit = "Diamonds"),
            Card(rank = "7", suit = "Clubs")
        ]

        deck.add_cards(cards)

        deck.shuffle()

        mock_shuffle.assert_called_once_with(cards)

    def test_removes_specified_number_of_cards_from_deck(self):
        ace   = Card(rank = "Ace", suit = "Clubs")
        eight = Card(rank = "8", suit = "Hearts")
        cards = [ace,eight]

        deck = Deck()
        deck.add_cards(cards)

        self.assertEqual(
            deck.remove_cards(1),
            [ace]
        )

        self.assertEqual(
            deck.cards,
            [eight]
        )