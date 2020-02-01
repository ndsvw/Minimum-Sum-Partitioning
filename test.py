import unittest
from min_sum_partitioning import min_sum_first_attempt, min_sum


class Test(unittest.TestCase):

    def assert_both_methods(self, l, sol):
        self.assertEqual(sol, min_sum_first_attempt(l))
        self.assertEqual(sol, min_sum(l))

    def testEmptyList(self):
        l = []
        self.assert_both_methods(l, 0)

    def testOneElement(self):
        l = [5]
        self.assert_both_methods(l, 5)

    def testTwoElements1(self):
        l = [1, 5]
        self.assert_both_methods(l, 4)

    def testTwoElements2(self):
        l = [5, 1]
        self.assert_both_methods(l, 4)

    def testSimpleCase1(self):
        l = [1, 6, 5, 11]
        self.assert_both_methods(l, 1)

    def testSimpleCase2(self):
        l = [36, 7, 46, 40]
        self.assert_both_methods(l, 23)

    def testSimpleCase3(self):
        l = [1, 4, 5, 7]
        self.assert_both_methods(l, 1)

    def testSimpleCase4(self):
        l = [1, 4, 5, 5, 10]
        self.assert_both_methods(l, 3)

    def testLargerCase(self):
        l = [37, 28, 16, 44, 36, 37, 43, 50, 22, 13, 28, 41, 10, 14, 27, 41, 27,
             23, 37, 12, 19, 18, 30, 33, 31, 13, 24, 18, 36, 30, 3, 23, 9, 20]
        self.assert_both_methods(l, 1)


if __name__ == "__main__":
    unittest.main()
