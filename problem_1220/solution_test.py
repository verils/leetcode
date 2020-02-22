import unittest

from problem_1220.solution import Solution


class MyTestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(5, Solution().count_vowel_permutation(1))

    def test2(self):
        self.assertEqual(10, Solution().count_vowel_permutation(2))

    def test3(self):
        self.assertEqual(68, Solution().count_vowel_permutation(5))

    def test4(self):
        # self.assertEqual(107871933390123834060683597780808227512929, Solution().count_vowel_permutation(144))
        self.assertEqual(18208803, Solution().count_vowel_permutation(144))


if __name__ == '__main__':
    unittest.main()
