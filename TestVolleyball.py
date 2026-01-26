import unittest
# import the code you want to test here
from volleyball import game_over, simulate_games, simulate_one_game, simulate_point
import random

class TestVolleyball(unittest.TestCase):

    def setUp(self) -> None:
        random.seed(20260126)
    
    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testGameOverRally_24_20(self) -> None:
        self.assertFalse(game_over(25, 24, 20))

    def testGameOverRally_20_24(self) -> None:
        self.assertFalse(game_over(25, 20, 24))

    def testGameOverRally_25_20(self) -> None:
        self.assertTrue(game_over(25, 25, 20))

    def testGameOverRally_20_25(self) -> None:
        self.assertTrue(game_over(25, 20, 25))

    def testGameOverRally_25_24(self) -> None:
        self.assertFalse(game_over(25, 25, 24))

    def testGameOverRally_26_26(self) -> None:
        self.assertFalse(game_over(25, 26, 26))

    def testGameOverRally_26_28(self) -> None:
        self.assertTrue(game_over(25, 26, 28))

    def testGameOverSideOut_14_10(self) -> None:
        self.assertFalse(game_over(15, 14, 10))

    def testGameOverSideOut_15_10(self) -> None:
        self.assertTrue(game_over(15, 15, 10))

    def testGameOverSideOut_15_14(self) -> None:
        self.assertFalse(game_over(15, 15, 14))

    def testGameOverSideOut_16_16(self) -> None:
        self.assertFalse(game_over(15, 16, 16))

    def testGameOverSideOut_16_18(self) -> None:
        self.assertTrue(game_over(15, 16, 18))

    def testSimulatePtServersWin(self) -> None:
        #print(random.random()) # 0.13352092893009526
        self.assertTrue(simulate_point(0.5))

    def testSimulatePtServersWinBarely(self) -> None:
        #print(random.random()) # 0.13352092893009526
        self.assertTrue(simulate_point(0.1336))

    def testSimulatePtServersLoseBarely(self) -> None:
        #print(random.random()) # 0.13352092893009526
        self.assertFalse(simulate_point(0.1335))

    def testSimulatePtServersLose(self) -> None:
        #print(random.random()) # 0.13352092893009526
        self.assertFalse(simulate_point(0.05))

    def testSimulateOneGame_p5_p5_rally(self) -> None:
        #simulate_one_game(.5, .5, 'rally')
        self.assertEqual(simulate_one_game(.5, .5, 'rally'), (22, 25))

    def testSimulateOneGame_p7_p7_rally(self) -> None:
        #simulate_one_game(.5, .5, 'rally')
        self.assertEqual(simulate_one_game(.7, .7, 'rally'), (25, 17))

    def testSimulateOneGame_p5_p5_sideout(self) -> None:
        self.assertEqual(simulate_one_game(.5, .5, 'sideout'), (16, 14))

    def testSimulateOneGame_p6_p6_sideout(self) -> None:
        self.assertEqual(simulate_one_game(.6, .6, 'sideout'), (8, 15))

    def testSimulateGames_p5_p5_rally_1(self) -> None:
        self.assertEqual(simulate_games(.5, .5, 1, 'rally'), 0)

    def testSimulateGames_p7_p7_rally_1(self) -> None:
        self.assertEqual(simulate_games(.7, .7, 1, 'rally'), 1)

    def testSimulateGames_p7_p7_rally_4(self) -> None:
        self.assertEqual(simulate_games(.7, .7, 4, 'rally'), 2)


if __name__ == '__main__':
    unittest.main()

