class Card():
    RANKS = (
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
        )
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")

    @classmethod
    def creates_standard_52_cards(cls):
        return [
            cls(rank = rank ,suit = suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __init__(self,rank,suit):
        if rank not in self.RANKS:
            raise ValueError("INVALID RANK,Rank can be one of following: {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError("INVALID SUIT,Suit can be one of following: {self.SUITS}")

        self.rank = rank
        self.rank_index = self.RANKS.index(rank)
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self,other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
            
        return self.rank_index < other.rank_index