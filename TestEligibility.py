import unittest
# import the code you want to test here
from eligibility import eligibleHR

class TestElgibility(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testHR_50_50(self) -> None:
        self.assertTrue(eligibleHR(50, 50)) # Generic True for both

    def testHR_20_3(self) -> None:
        self.assertFalse(eligibleHR(20, 3)) # Generic False for both

    def testHR_18_18(self) -> None:
        self.assertFalse(eligibleHR(18, 18)) # Generic False age, generic True citizenship

    def testHR_50_3(self) -> None:
        self.assertFalse(eligibleHR(50, 3)) # Generic True age, generic False citizenship

    def testHR_30_35(self) -> None:
        with self.assertRaises(ValueError):
            eligibleHR(30, 35)              # Citizenship > age

    def testHR_25_25(self)-> None:
        self.assertTrue(eligibleHR(25, 25)) # Border True age, generic True citizenship

    def testHR_24_24(self) -> None:
        self.assertFalse(eligibleHR(24, 24)) # Border False age, generic True citizenship

    def testHR_50_6(self) -> None:
        self.assertFalse(eligibleHR(50, 6)) # Generic True age, border False citizenship

    def testHR_50_7(self) -> None:
        self.assertTrue(eligibleHR(50, 7)) # Generic True age, border True citizenship

if __name__ == '__main__':
    unittest.main()

