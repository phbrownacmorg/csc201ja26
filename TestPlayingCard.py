import unittest
# import the code you want to test here
from PlayingCard import PlayingCard

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testSuitAccessor(self) -> None:
        for suit in PlayingCard.SUITS:
            with self.subTest(suit=suit):
                self.assertEqual(PlayingCard('5', suit).suit(), suit)

    def testRankAccessor(self) -> None:
        for rank in PlayingCard.RANKS:
            with self.subTest(rank=rank):
                self.assertEqual(PlayingCard(rank, 'hearts').rank(), rank)

    def testConstructorBadRank(self) -> None:
        with self.assertRaises(ValueError) as cm:
            PlayingCard('scullion', 'diamonds')
        self.assertEqual(cm.exception.args[0], 'Invalid rank: scullion')

    def testConstructorBadSuit(self) -> None:
        with self.assertRaises(ValueError) as cm:
            PlayingCard('ace', 'cockroaches')
        self.assertEqual(cm.exception.args[0], 'Invalid suit: cockroaches')

    def testStr(self) -> None:
        for rank in PlayingCard.RANKS:
            for suit in PlayingCard.SUITS:
                with self.subTest(rank=rank, suit=suit):
                    #print(PlayingCard(rank, suit))
                    self.assertEqual(str(PlayingCard(rank, suit)), f'{rank} of {suit}')

    def testEq(self) -> None:
        for rank1 in PlayingCard.RANKS:
            for suit1 in PlayingCard.SUITS:
                card1 = PlayingCard(rank1, suit1)
                for rank2 in PlayingCard.RANKS:
                    for suit2 in PlayingCard.SUITS:
                        card2 = PlayingCard(rank2, suit2)
                        with self.subTest(rank1=rank1, suit1=suit1, rank2=rank2, suit2=suit2):
                            self.assertEqual(card1 == card2, rank1 == rank2 and suit1 == suit2)

    def testLt(self) -> None:
        for rank1 in PlayingCard.RANKS:
            for suit1 in PlayingCard.SUITS:
                card1 = PlayingCard(rank1, suit1)
                for rank2 in PlayingCard.RANKS:
                    for suit2 in PlayingCard.SUITS:
                        card2 = PlayingCard(rank2, suit2)
                        with self.subTest(rank1=rank1, suit1=suit1, rank2=rank2, suit2=suit2):
                            rankIdx1 = PlayingCard.RANKS.index(rank1)
                            rankIdx2 = PlayingCard.RANKS.index(rank2)
                            suitIdx1 = PlayingCard.SUITS.index(suit1)
                            suitIdx2 = PlayingCard.SUITS.index(suit2)
                            self.assertEqual(card1 < card2,
                                             (rankIdx1 < rankIdx2) or (rank1 == rank2 and suitIdx1 < suitIdx2))

    def testMakeDeck(self) -> None:
        deck = PlayingCard.makeDeck()
        self.assertEqual(len(deck), 52)
        for rank in PlayingCard.RANKS:
            for suit in PlayingCard.SUITS:
                with self.subTest(rank=rank, suit=suit):
                    self.assertEqual(deck.count(PlayingCard(rank, suit)), 1)

    def testRankIndex(self) -> None:
        for rank in PlayingCard.RANKS[:9]: # Numeric ranks
            with self.subTest(rank=rank):
                self.assertEqual(PlayingCard(rank, 'hearts').rankIdx(), int(rank) - 2)
        self.assertEqual(PlayingCard('jack', 'hearts').rankIdx(), 9)
        self.assertEqual(PlayingCard('queen', 'hearts').rankIdx(), 10)
        self.assertEqual(PlayingCard('king', 'hearts').rankIdx(), 11)
        self.assertEqual(PlayingCard('ace', 'hearts').rankIdx(), 12)

if __name__ == '__main__':
    unittest.main()

