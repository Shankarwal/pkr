class FiveCardRankInARowValidator():
    @property
    def _collection_of_five_straight_cards_in_a_row(self):
        index = 0
        final_index = len(self.cards) - 1
        collection_of_five_straight_cards_in_a_row = []

        while index + 4 <= final_index:
            next_five_cards = self.cards[index : index +5]
            rank_indexes    = [card.rank_index for card in next_five_cards]
            if self._every_element_increasing_by_one(rank_indexes):
                collection_of_five_straight_cards_in_a_row.append(next_five_cards)

            index += 1

        return collection_of_five_straight_cards_in_a_row


    def _every_element_increasing_by_one(self, rank_indexes):
        start_index = rank_indexes[0]
        end_index   = rank_indexes[-1]
        straight_indexes = list(
            range(start_index, end_index + 1)
        )
        return rank_indexes == straight_indexes
    