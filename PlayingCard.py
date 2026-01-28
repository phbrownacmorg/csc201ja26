# CONVENTION: Classes are defined in a file that has the same name as the class.

class PlayingCard: # CONVENTION: Class names are in CamelCase, where the first
    # letter of each word is capitalized.
    """Class to represent a playing card of the traditional French pattern, as
        commonly used in English-speaking countries to play blackjack, poker,
        solitaire, hearts, war, and a whole host of other card games.  A 
        PlayingCard is immutable once created."""
    
    # CONVENTION: Constants, especially class-level constants, have names in ALL_CAPS.
    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')
    RANKS = tuple([str(i) for i in range(2, 11)]) + ('jack', 'queen', 'king', 'ace')

    # Constructor
    def __init__(self, rank: str, suit: str) -> None:
        """Construct a new PlayingCard of the given RANK and SUIT."""
        if rank not in self.RANKS:
            raise ValueError(f'Invalid rank: {rank}')
        elif suit not in self.SUITS:
            raise ValueError(f'Invalid suit: {suit}')
        self._rank = rank
        self._suit = suit
    
    # ----------- Accessor methods -------------------

    def suit(self) -> str:
        return self._suit
    
    def rank(self) -> str:
        return self._rank
    
    def rankIdx(self) -> int:
        return self.RANKS.index(self.rank())
    
    def __str__(self) -> str:
        return self.rank() + ' of ' + self.suit()

    def __eq__(self, other: object) -> bool:
        result = True
        if not hasattr(other, 'rank') or self.rank() != other.rank(): ## type: ignore
            result = False
        elif not hasattr(other, 'suit') or self.suit() != other.suit(): ## type: ignore
            result = False
        return result
    
    # Primarily for sorting
    def __lt__(self, other: 'PlayingCard') -> bool:
        try:
            result = self.rankIdx() < self.RANKS.index(other.rank())
            if self.rank() == other.rank():
                result = (self.SUITS.index(self.suit()) < self.SUITS.index(other.suit()))
        except IndexError: # other.rank() isn't in self.RANKS or other.suit() isn't in self.SUITS
            raise ValueError(f'Incompatible ranks and suits: {self}, {other}')
        return result

    # ----------- Class method ----------------------

    @classmethod
    def makeDeck(cls) -> list['PlayingCard']:
        deck: list[PlayingCard] = []
        for rank in cls.RANKS:
            for suit in cls.SUITS:
                deck.append(PlayingCard(rank, suit))
        return deck
