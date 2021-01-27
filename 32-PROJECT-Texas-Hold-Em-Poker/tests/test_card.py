import unittest 
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank= "6",suit = "Hearts")

        self.assertEqual(
            card.rank,
            "6"
        )

    def test_has_suit(self):
        card = Card(rank= "6",suit = "Hearts")

        self.assertEqual(
            card.suit,
            "Hearts"
        )
    
    def test_knows_its_rank_indesx(self):
        card = Card(rank = "Jack", suit = "Hearts")
        self.assertEqual(card.rank_index, 9)

    def test_has_string_representation_with_rank_and_suit(self):
        card = Card(rank= "King",suit = "Clubs")

        self.assertEqual(
            str(card),
            "King of Clubs"
        )

    def test_has_technical_representation(self):
        card = Card(rank= "8",suit = "Diamonds")

        self.assertEqual(
            repr(card),
            "Card('8', 'Diamonds')"
        )

    def test_has_four_possible_suits(self):
        self.assertEqual(
            Card.SUITS,
            ("Clubs", "Diamonds", "Hearts", "Spades")
        )

    def test_has_thirteen_possible_ranks(self):
        self.assertEqual(
            Card.RANKS,
            (
                "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Jack", "Queen", "King", "Ace"
            )
        )

    def test_card_only_allows_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two", suit = "Hearts")

    def test_card_only_allows_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "5", suit = "Heart")

    def test_creates_standard_52_cards(self):
        cards = Card.creates_standard_52_cards()
        self.assertEqual(len(cards),52)

        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Clubs")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit = "Spades")
        )

    def test_figures_out_if_two_cards_are_equal(self):
        self.assertEqual(
            Card(rank = "Ace", suit = "Spades"),
            Card(rank = "Ace", suit = "Spades")
        )

    def test_card_can_sort_itself_with_another_one(self):
        queen_of_spades = Card(rank = "Queen", suit = "Spades")
        king_of_hearts = Card(rank = "King", suit = "Hearts")
        evaluation = queen_of_spades < king_of_hearts

        self.assertEqual(
            evaluation,
            True
        )

    def test_sorts_cards(self):
        two_of_spades   = Card(rank = "2", suit = "Spades")
        five_of_clubs   = Card(rank = "5", suit = "Clubs")
        five_of_hearts  = Card(rank = "5", suit = "Hearts")
        eight_of_clubs  = Card(rank = "8", suit = "Clubs")
        ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")

        unsorted_cards = [
            eight_of_clubs,
            five_of_hearts,
            five_of_clubs,
            ace_of_diamonds,
            two_of_spades
        ]

        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_clubs,
                five_of_hearts,
                eight_of_clubs,
                ace_of_diamonds
            ]
        )    