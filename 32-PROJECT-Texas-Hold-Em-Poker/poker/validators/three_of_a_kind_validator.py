from poker.validators import RankValidator

class ThreeOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Three of a Kind"

    def is_valid(self):
        rank_with_three_of_a_kind = self._rank_with_counts(3)
        return len(rank_with_three_of_a_kind) == 1

    def valid_cards(self):
        rank_with_three_of_a_kind = self._rank_with_counts(3)
        cards = [card for card in self.cards if card.rank in rank_with_three_of_a_kind.keys()]
        return cards
