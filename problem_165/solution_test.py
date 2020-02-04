import unittest

from problem_165.solution import Solution


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(-1, Solution().compare_version('0.1', '1.1'))

    def test2(self):
        self.assertEqual(1, Solution().compare_version('1.0.1', '1'))

    def test3(self):
        self.assertEqual(-1, Solution().compare_version('7.5.2.3', '7.5.3'))

    def test4(self):
        self.assertEqual(0, Solution().compare_version('1.01', '1.001'))

    def test5(self):
        self.assertEqual(0, Solution().compare_version('1.0', '1.0.0'))


if __name__ == '__main__':
    unittest.main()
