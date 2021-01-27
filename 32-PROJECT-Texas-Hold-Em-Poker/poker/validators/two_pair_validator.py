from poker.validators import RankValidator

class TwoPairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name  = "Two Pair"

    def is_valid(self):
        rank_with_pairs = self._rank_with_counts(2)
        return len(rank_with_pairs) >= 2

    def valid_cards(self):
        rank_with_pairs = self._rank_with_counts(2)
        cards = [card for card in self.cards if card.rank in rank_with_pairs.keys()]
        return cards
