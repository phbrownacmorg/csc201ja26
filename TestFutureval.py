import unittest
# import the code you want to test here
from futureval import calcBalances

class TestFutureval(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testBal_1000_1_3(self) -> None:
        expected = [1000, 1010, 1020.10, 1030.301]
        balanceList = calcBalances(1000, .01, 3)
        #print(balanceList)
        for i in range(len(balanceList)):
            with self.subTest(i=i):
                self.assertAlmostEqual(balanceList[i], expected[i])

    def testBal_2000_2_3(self) -> None:
        expected = [2000, 2040, 2080.80, 2122.416, 2164.86432]
        balanceList = calcBalances(2000, .02, 4)
        #print(balanceList)
        for i in range(len(balanceList)):
            with self.subTest(i=i):
                self.assertAlmostEqual(balanceList[i], expected[i])




if __name__ == '__main__':
    unittest.main()

