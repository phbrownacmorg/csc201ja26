import unittest
# import the code you want to test here
from quadratic import findRoots, determinant

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testDeterminantZero(self) -> None:
        self.assertAlmostEqual(determinant(1, 0, 0), 0)

    def testDeterminant4(self) -> None:
        self.assertAlmostEqual(determinant(1, 4, 3), 4)

    def testDeterminant9(self) -> None:
        self.assertAlmostEqual(determinant(1, 4, 1.75), 9)

    def testDeterminant16(self) -> None:
        self.assertAlmostEqual(determinant(1, 5, 2.25), 16)

    def testDeterminant_n8(self) -> None:
        self.assertAlmostEqual(determinant(1, 2, 3), -8)
    
    def testFindRoots1_0_0(self) -> None:
        roots = findRoots(1, 0, 0)
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], 0)

    def testFindRoots1_4_3(self) -> None:
        roots = findRoots(1, 4, 3)
        self.assertAlmostEqual(roots[0], -1)
        self.assertAlmostEqual(roots[1], -3)

    def testFindRoots1_4_1p75(self) -> None:
        roots = findRoots(1, 4, 1.75)
        self.assertAlmostEqual(roots[0], -.5)
        self.assertAlmostEqual(roots[1], -3.5)

    def testFindRoots1_2_3(self) -> None:
        # Determinant is -8
        # Just check for the exception type
        with self.assertRaises(ValueError): 
            findRoots(1, 2, 3) # Run the code that will raise the exception
    
    def testFindRoots1_n2_3(self) -> None:
        # Check the message as well
        with self.assertRaises(ValueError) as cm: # Create a context manager, which has the exception
            findRoots(1, -2, 3) # Run the code that will raise the exception
        self.assertEqual(cm.exception.args[0], 'There are no real roots.') # Compare the message as a string


if __name__ == '__main__':
    unittest.main()

