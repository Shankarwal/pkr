import unittest
from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator 

class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank = "Jack", suit = "Spades"),
            Card(rank = "Ace", suit = "Clubs")
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            "Jack of Spades, Ace of Clubs"
        )

    def test_recieves_and_stores(self):
        ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        jack_of_spades = Card(rank = "Jack", suit = "Spades")

        cards = [
            ace_of_clubs,
            jack_of_spades
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
                jack_of_spades,
                ace_of_clubs
            ]
        )

    def test_interacts_with_validators_to_get_wnning_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator,)

        ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        cards = [ace_of_hearts, ace_of_spades]

        hand = HandWithOneValidator()
        hand.add_cards(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            (0, "Pair", [ace_of_hearts, ace_of_spades])
        )