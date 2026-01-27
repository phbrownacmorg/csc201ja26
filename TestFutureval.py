import unittest
import contextlib
import io
# import the code you want to test here
from futureval import calcBalances, printTable

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

    def testPrintTable(self) -> None:
        printOut = """Period             Interest                 Balance
-----------------------------------------------------
Initial                                 $    1,000.00
 1              $      50.00            $    1,050.00
 2              $      52.50            $    1,102.50
 3              $      55.12            $    1,157.62
 4              $      57.88            $    1,215.51"""
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            printTable([1000, 1050, 1102.50, 1157.625, 1000*1.05**4])
        self.assertEqual(out.getvalue(), printOut + '\n')




if __name__ == '__main__':
    unittest.main()

