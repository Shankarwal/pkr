from poker.validators import RankValidator

class FourOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Four of a Kind"

    def is_valid(self):
        rank_with_four_of_a_kind = self._rank_with_counts(4)
        return len(rank_with_four_of_a_kind) == 1

    def valid_cards(self):
        rank_with_four_of_a_kind = self._rank_with_counts(4)
        cards = [card for card in self.cards if card.rank in rank_with_four_of_a_kind.keys()]
        return cards