from PlayingCard import PlayingCard

class PokerHand:
    """Class to represent a five-card poker hand."""

    def __init__(self, card1: PlayingCard, card2: PlayingCard, card3: PlayingCard,
                 card4: PlayingCard, card5: PlayingCard) -> None:
        self._cards: list[PlayingCard] = [card1, card2, card3, card4, card5]
        self._cards.sort()
        self._rankCount: list[int] = [0] * len(PlayingCard.RANKS)
        for card in self._cards:
            self._rankCount[card.rankIdx()] = self._rankCount[card.rankIdx()] + 1

    def __str__(self) -> str:
        result = '['
        for card in self._cards:
            result += str(card) + ', '
        return result[:-2] + ']'


    def hasPair(self) -> bool:
        """Return True if the hand has just one pair."""
        return self._rankCount.count(2) == 1
    
    def hasTwoPair(self) -> bool:
        """Return True if the hand has two pair."""
        return self._rankCount.count(2) == 2
    
    def hasThreeOfAKind(self) -> bool:
        """Return True if the hand has three of a kind."""
        return self._rankCount.count(3) == 1
    
    def hasFourOfAKind(self) -> bool:
        """Return True if the hand has four of a kind."""
        return self._rankCount.count(4) == 1

    def isFullHouse(self) -> bool:
        """Return True if the hand is a full house."""
        return self.hasThreeOfAKind() and self.hasPair()

    def isFlush(self) -> bool:
        """Return True if the hand is a flush."""
        flush = True
        suit = self._cards[0].suit()
        for card in self._cards[1:]:
            if card.suit() != suit:
                flush = False
        return flush
    
    def isStraight(self) -> bool:
        straight = True
        firstRank = self._cards[0].rankIdx() # Because cards are sorted, this one has the lowest rank
        for r in range(firstRank, firstRank+5):
            if self._rankCount[r] != 1:
                straight = False
        return straight

    def isStraightFlush(self) -> bool:
        return self.isStraight() and self.isFlush()
    
    def isRoyalFlush(self) -> bool:
        return self.isStraightFlush() and self._cards[0].rank() == '10'
    
    #def characterize(self) -> str:

