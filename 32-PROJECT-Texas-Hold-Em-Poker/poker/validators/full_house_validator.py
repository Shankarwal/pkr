from poker.validators import ThreeOfAKindValidator, PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        return ThreeOfAKindValidator(cards = self.cards).is_valid() and PairValidator(cards = self.cards).is_valid()

    def valid_cards(self):
        rank_with_pairs = ThreeOfAKindValidator(cards = self.cards).valid_cards()
        rank_with_three_of_a_kind = PairValidator(cards = self.cards).valid_cards()
        all_cards = rank_with_pairs + rank_with_three_of_a_kind
        all_cards.sort()
        return all_cards