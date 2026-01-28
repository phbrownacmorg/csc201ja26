import unittest
# import the code you want to test here
from PlayingCard import PlayingCard
from PokerHand import PokerHand


class TestPokerHand(unittest.TestCase):

    def setUp(self) -> None:
        ace_hearts = PlayingCard('ace', 'hearts')
        king_hearts = PlayingCard('king', 'hearts')
        queen_hearts = PlayingCard('queen', 'hearts')
        jack_hearts = PlayingCard('jack', 'hearts')
        ten_hearts = PlayingCard('10', 'hearts')
        ten_clubs = PlayingCard('10', 'clubs')
        ten_diamonds = PlayingCard('10', 'diamonds')
        ten_spades = PlayingCard('10', 'spades')
        nine_hearts = PlayingCard('9', 'hearts')
        jack_diamonds = PlayingCard('jack', 'diamonds')


        self._royal_flush = PokerHand(ten_hearts, jack_hearts, queen_hearts, king_hearts, ace_hearts)
        self._straight_flush = PokerHand(nine_hearts, ten_hearts, jack_hearts, queen_hearts, king_hearts)
        self._4_of_a_kind = PokerHand(ten_hearts, ten_clubs, ten_diamonds, ten_spades, jack_hearts)
        self._straight_no_flush = PokerHand(nine_hearts, ten_spades, jack_hearts, queen_hearts, king_hearts)
        self._flush_no_straight = PokerHand(nine_hearts, ten_hearts, jack_hearts, queen_hearts, ace_hearts)
        self._full_house = PokerHand(ten_clubs, ten_diamonds, ten_hearts, jack_diamonds, jack_hearts)
        self._3_of_a_kind = PokerHand(ten_clubs, ten_diamonds, ten_hearts, jack_diamonds, queen_hearts)
        self._2_pair = PokerHand(ten_clubs, ten_diamonds, nine_hearts, jack_diamonds, jack_hearts)
        self._pair = PokerHand(nine_hearts, ten_clubs, jack_hearts, jack_diamonds, king_hearts)

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testRoyalFlushT(self) -> None:
        self.assertTrue(self._royal_flush.isRoyalFlush())

    def testRoyalFlushF9(self) -> None:
        self.assertFalse(self._straight_flush.isRoyalFlush())

    def testRoyalFlushFnoFlush(self) -> None:
        self.assertFalse(self._4_of_a_kind.isRoyalFlush())

    def testStraightFlushT(self) -> None:
        self.assertTrue(self._straight_flush.isStraightFlush())

    def testStraightFlushFnoFlush(self) -> None:
        self.assertFalse(self._straight_no_flush.isStraightFlush())

    def testStraightFlushFnoStraight(self) -> None:
        self.assertFalse(self._flush_no_straight.isStraightFlush())

    def testStraightT(self) -> None:
        self.assertTrue(self._straight_no_flush.isStraight())
    
    def testStraightF(self) -> None:
        self.assertFalse(self._flush_no_straight.isStraight())

    def testFlushT(self) -> None:
        self.assertTrue(self._flush_no_straight.isFlush())

    def testFlushF(self) -> None:
        self.assertFalse(self._straight_no_flush.isFlush())

    def testFullHouseT(self) -> None:
        self.assertTrue(self._full_house.isFullHouse())

    def testFullHouseFnoPair(self) -> None:
        self.assertFalse(self._3_of_a_kind.isFullHouse())

    def testFullHouseFno3(self) -> None:
        self.assertFalse(self._pair.isFullHouse())

    def test4OfAKindT(self) -> None:
        self.assertTrue(self._4_of_a_kind.hasFourOfAKind())

    def test4OfAKindF3(self) -> None:
        self.assertFalse(self._3_of_a_kind.hasFourOfAKind())

    def test3OfAKindT(self) -> None:
        self.assertTrue(self._3_of_a_kind.hasThreeOfAKind())

    def test3ofAKindF4(self) -> None:
        self.assertFalse(self._4_of_a_kind.hasThreeOfAKind()) # OK, it's odd
    
    def test3ofAKindF2(self) -> None:
        self.assertFalse(self._pair.hasThreeOfAKind())
   
    def test2PairT(self) -> None:
        self.assertTrue(self._2_pair.hasTwoPair())

    def test2PairF(self) -> None:
        self.assertFalse(self._pair.hasTwoPair())

    def testPairT(self) -> None:
        self.assertTrue(self._pair.hasPair())

    def testPairF(self) -> None:
        self.assertFalse(self._royal_flush.hasPair())

    def testStrRoyalFlush(self) -> None:
        self.assertEqual(str(self._royal_flush), 
                         '[10 of hearts, jack of hearts, queen of hearts, king of hearts, ace of hearts]')
    
    def testStr2Pair(self) -> None:
        self.assertEqual(str(self._2_pair),
                         '[9 of hearts, 10 of clubs, 10 of diamonds, jack of diamonds, jack of hearts]')


if __name__ == '__main__':
    unittest.main()

