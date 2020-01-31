import unittest
from problem_1032.stream_checker import StreamChecker
import json


class MyTestCase(unittest.TestCase):

    def test1(self):
        stream_checker = StreamChecker(['cd', 'f', 'kl'])
        self.assertFalse(stream_checker.query('a'))
        self.assertFalse(stream_checker.query('b'))
        self.assertFalse(stream_checker.query('c'))
        self.assertTrue(stream_checker.query('d'))
        self.assertFalse(stream_checker.query('e'))
        self.assertTrue(stream_checker.query('f'))
        self.assertFalse(stream_checker.query('g'))
        self.assertFalse(stream_checker.query('h'))
        self.assertFalse(stream_checker.query('i'))
        self.assertFalse(stream_checker.query('j'))
        self.assertFalse(stream_checker.query('k'))
        self.assertTrue(stream_checker.query('l'))

    def test2(self):
        stream_checker = StreamChecker(['ab', 'ba', 'aaab', 'abab', 'baa'])

        query = [["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"],
                 ["a"], ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"], ["a"],
                 ["a"], ["a"]]
        expected = [False, False, False, False, False, True, True, True, True, True, False, False, True, True, True,
                    True, False, False, False, True, True, True, True, True, True, False, True, True, True, False]

        self.assertEqual(len(query), len(expected))
        for i in range(len(query)):
            self.assertEqual(expected[i], stream_checker.query(query[i][0]), 'query index: {}'.format(i))

    def test3(self):
        stream_checker = StreamChecker(["abaa", "abaab", "aabbb", "bab", "ab"])

        query = [["a"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["b"], ["b"], ["a"], ["a"], ["a"], ["a"], ["b"],
                 ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["a"], ["a"], ["a"], ["b"],
                 ["a"], ["b"], ["b"], ["b"], ["a"], ["a"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"]]
        expected = [False, False, True, False, True, False, False, True, False, False, False, False, False, True, False,
                    True, False, False, False, True, False, False, False, False, False, False, False, True, False, True,
                    False, False, False, False, True, False, True, False, True, False]

        self.assertEqual(len(query), len(expected))
        for i in range(len(query)):
            self.assertEqual(expected[i], stream_checker.query(query[i][0]), 'query index: {}'.format(i))

    def test4(self):
        stream_checker = StreamChecker(["babbaabababbbbabbaaaaaaabbbbaababbbbabaabbaabaabaabbbabbabbbaabaaabbba",
                                        "bbabbbaababbaababbbabaabaabaabbbbaabbaabbaaababbabbbbbabbbbbbbaaaaaabaaabaaaaabbabbbaba",
                                        "aaabaaabaabbbaababbbaaabababaaaaababbbbabaaaaaaaabbaabbbaababbbbababbabaababaabababaabaabbababaaa",
                                        "abbabbabbbbaaabababbbbaaaaabaaaaaaaaaabbbabbbababbabbb",
                                        "bbaabbbaabbaaababbaabaaaabbabbbbababaaabbbbbabaabbaabbaaababbaabbab",
                                        "aaaaaababbbbbbbabaaabbabbbaabbaababbbbbbaabbbbababbbbabaabababbabbbbaaabbaababaabaaaaabbbbaa",
                                        "baaabbabbbbaabbabbbbbbbbbbaabbabaabbabaaabababbbbaaaabbb",
                                        "aaabaabbaabbbabbbaabbabbbbbabaabbabbbabaabbaaabbbaaababaabbabbbabbabaaabbbaaaababbaaaa",
                                        "abbaaaababbbbaabbbabaaaaaabbabbabaaaabbbbbaaabaaababaaabababbabbbaabbbabbaaaaaabbbabbabbba",
                                        "aaaaaabbaabbbabbaabbabbbaaabaaabababbaaaaababaabbbaabbaabbabbbaabaaaabbbaababaaaaaababa",
                                        "bbbabaababbbbbaabbbbaaabbababbbbbbaabbabbaabbbaaabababaabaaaabaa",
                                        "babaababaaaaabbbbaaaaabaaababbaaabababbbbaabaabbaaabbb",
                                        "aaaabbbbaaaabbaaabbbaaabbbabaabbbaaabaaababaaababaababbbabbaabbaabbbbababbbaaaaaabaabaabbbbbbaba",
                                        "aabaabbabbbabaaaababbaaababbabababbabaabbaaabbababbbbaaaaaaabbabbbbaa",
                                        "bbabbbbbabaababaabaaabaabbbbbbbaaaabbbbaababaaaaaabababbabbbaabb",
                                        "bbbbbabbbabaaabaabbaaaabbbabbbbbbaababbaabaaaabbabaabbbabbbbbbaabababaaabaaaaabaabababaabbabbbabb",
                                        "aabaababaababaabbbabbaaabbbbabbbbababbaaaaabaaabaaaaabaaaaaabbabbbbaabb",
                                        "babbbabbbabbababbbabaaabbaaaabaabaabaaaabbabbaababbaababaaabaab",
                                        "aabaababbabbbabbabababaabbbaaababbbabbbbbbbaababbbbaaabbaaababaaaaabbaabbaababba",
                                        "bbbaaaabaaaabbbbbababaabababbabababaaabbbbaaaabbbbbabaaaabbbbbaabbaabbabbabaaaabaabbababbaabbaaaa",
                                        "abbabbbbbbaabbabaaabaabbbbbbabbbaaabaabbabbbbaaabbbbbaaaabaaaabaaabbbaaabaaaba",
                                        "ababababbbabababbbbbbbbabbbabbbbabbbaabbbbbabbabaabababbbaba",
                                        "babbabbbaabbaababbbababaaabbbbbbbaabaabbaaaababbabbbaabbaaaabbbaabaaaabbabaabbaabaabba",
                                        "bbaaabbababaaabbaaaabbbbbbaababbaabbaaabbbaaaaabbaabaaabbbabbbaaabaaaaaabbbababbabbbaabbbabbbabbaab",
                                        "baabababbbbabaaaaaaaabaaaabaababaaababbbaababbaaabababb",
                                        "baaabbabaaaaaabaaabbbaaaaabbababbbaaabbbabbaababbbababaaabbbaaaaaaabaaabbabbabbaaaaababbba",
                                        "aaaabbbbaaaabaaabbbbabaabaaabbaaabbbbabbababbbbbbbaaaa",
                                        "aaabbaaaabbbaababbabaaabaababbbbaaabababbaabbbaabbaabbbaaaaaab",
                                        "aaaabababaaabbbbaabbabaaaabbbbbbaabbaabbaababbaaababbbbabaaa",
                                        "babbabaaaaabbabaaaaaaaabababbababaabbbbaaabaabbaabbbbbbaaabbaaabaabbaa",
                                        "baaabbbbbababbbbbabbbbbababbabbbbbbbaabbababbaabbbbbaabbbbbababba",
                                        "aaaaababaabaaabbaaaaaabbbaaabbababaaabbabaaaaabbbaabbaabaaaabbbbbb",
                                        "bbababbbbaaabaaababbaabbaababaaabbaaabbbaaaabaabbaabbabbbababaabaaababbbaabbaaa",
                                        "bbbbbabbaababbbaabaabaaabbaabbbababbbbbaabaaaabbaabaaaabaaabaaababaabbbaaaabbabbbabbaab",
                                        "abbbabbbababaababaaabaaaabaabbaaabbbaabbbaaaaaabaaababbbbaabaaabaabbaaa",
                                        "bbbabaaabaaaaaabbbaaabbbaaaababbabababababaaabbbbbabaabb",
                                        "aababbabbbbabbbabbbbbbbbbabaaaaabaaaaababbaaabbbbaababbbaaaaaaa",
                                        "aabababaaaababbababbabaaabaaabaaabaabbbaabbaaabbbbbababbaaaabaabbabbabaaaaabbbababababbabaaaabba",
                                        "babbabbaabaabbbaaabbabbbababbbbabababbbbbaababbbbabbababbbabaabaababbababababaabaaaaaabbababbaaaabbb",
                                        "aaababaaaabbabaabbabaabbbbbabaabbaaabbbabbbaababbaaaabbbabbabbabaababbabbaabaaa",
                                        "baaababbbaaabaabbabbbbabbbbaabbaaaaaaaabbaabbabaaaaaabaaaaaaabaaabbaaaabbaabbbbabbb",
                                        "aaabbaabaababbabbbbbabbaaaabaabaaaaabaaaabaabaababbaa",
                                        "bbbbbbabbaaaaabbababbaabbbaaaababbababaaabaabbabbbaababbbaaaabbbaababababaababba",
                                        "aabaabbaaabbbbbaaaaabaababbabaabbbbaabbaaaaaaabbbbbbbaaabbbabaaabbbbababaabbaabaaaabbbbababababbab",
                                        "bbbaaaababaaaaababbabbbbbbbbbbaababbaabbaabababababbbabbbbaaabbabbbaaabbbbbbabab",
                                        "babaaabbbabbbabbabaabababaabbaaabbbbabbbaaabbbababaaaaabaabbba",
                                        "ababbabbabbbbbbaaaabbbbbaaaabbaaaababaaabaabbaaaaaabbaaa",
                                        "abbbbbbbbaaaabbbaaaaaaaaabbbaabbaaabaaabbaabaaababbbbbabbababbbbabbabbabbbabbaaababbaabaabab",
                                        "bbaaaaababbbbbaabbaabbaabbaaabbaaabbbbbbbbbbaaabaababa",
                                        "abaabbaabbabbbbbbbbbbbaaabaabbbbabaaabbbaabbbabbababb",
                                        "aabaaaaabbaabbbbbabaabbbabbaababbaaaaaabaaababbabbbbbaaabbaabaababaaaabaab",
                                        "bbaaaaaabbabbbbabbbaabaaaaabaabbbabbbaabbbbabbbbaaabbbbbaaabaababbabbabba",
                                        "aabbaaaaaaaaaabababaaaabbbbbabbabbaababaabbababbbaabbaabaaabbaababaabaabaabbabaaaaa",
                                        "bbbbabbbababbbbaabbabaababbbbbabbbbaaabaaaaaababaababbaaaabaabaababbbbbbababaabbbaabba",
                                        "bbbabbaaababbbbbbabaaabaaaaaaaabaaaaabaabbbabbbabbaababbbbbabbbbaaaaabb",
                                        "bbaabaabbabbabbbaaabaabaababaaaabbaabbaaaabaaaaabbabbba",
                                        "abaaaaaaaababbbabaaabaabbaaabaaaaabababbbabbaabbaa",
                                        "abbabbaababaaaaaaaabaabbaaabbbbabaaabaaaabaababbabbaabbaabbaaa",
                                        "aaaabbbabbabababbabbbbbbbababbbaabbababbbaaabbaaaa",
                                        "aaaaaababaaaabaabbaabbaabababbabbaaaaaabbbbaabbabaabaaabbbbbbaaaaabaabaabbabbaababbbbaaaabbabaab",
                                        "abbababbababbbaaabbaabbabbbaaaabbaabaabbaabbbbbabb",
                                        "abababbaaabaaabbaababbaabbaaaaaaaabbaaaabababababbaaabbaababbbaabbaabbabbbbbbbaabaa",
                                        "abaaabbbbbaaaabbbababababaaaabaabaaaababbababbabab",
                                        "aaaabbbaaaababaabaaaaababbabababbaabaabbbaaaabbbbabbaaabababbabbabbbbbaaaaba",
                                        "abbbbababbaaaabababbaaabaaaabaabaaaabbbaabababbbbaaabbaabbaababbbaaabbbaaabbaaababbaaabababbba",
                                        "abbbbabbbaaaabbabbabaaaabababaaababaabbabaabaababbaabbaaaabbaabba",
                                        "babaaabaaaaabaabaabababaaabbabaaababbbbbababaaaababbbbaaaabaaaabbbaaababbbaababbaabaaabaaaabbbaa",
                                        "aabbaabbbabaabaabbabbbaabbbbbbaabaabbabbaabababbbaabbbbaaaabbbabaabbaabaab",
                                        "ababababbababbaaaababbbbaabbbbbbabbaaabaabbaabababbbaaaabbabaabbbaabbaababbabbabbabaaaaaaaabaaaa",
                                        "abaababbabaaabbabaabbbaaabaabababaaaaababababbbaababbbbabbbaabaaababbaabaaaaab",
                                        "babaabaabbbabbbbbabbabaabbbaabbaaabbbbbbbbbaabbaaabaabbabaabbaab",
                                        "aabbbbaaaaaaabaaaaaabbbababaaaabbabaaabababaabababbabbbabaaaaabbababbbabbaabaabaababbababa",
                                        "abbaaaabbabbbaaaabaaaabbaaaabbaabaaababaaaaabbababbbabaabaaabbbaabababbabbbbababbbba",
                                        "aaabbbbaabababaaababbabbaabbbbaaaabbbaababbaabaabbaaaaabbaabbbbaaaabbbbabaaaaabbaaababbba",
                                        "aaabbabaaaaaabbbaaaaaaabbaaaaaababbbbbaababbabbbbaabaaaaabbbbaaabaababbbaabbabbaaabababba",
                                        "abbbbaaabbbabaababbbbaabbbbabababaabbbaaabaaabaabababababbbbbbbaaabbabaaabbbaabababaaabbbbaaba",
                                        "aabbbbbaaabbaaabbaabbaaabbbbbaabababbbbbbabbaabbabbaabbaabaaaaabbaaabbaaaabbaabb",
                                        "abbbbbbabbabaaabbabaababbbbbaaabbaaaababbaaaabbbbaababbabaaaba",
                                        "babaaaaaaaabbbabaaabbbbaaaaaabaabaabbbaaaaaaaababbbbabbabbbbbaaa",
                                        "aaabaaabbaaababaabaaaabbaabbbababaaabbabbabaabbbaabaabbbbbaabbbabababbabaabababaabab",
                                        "baabaabbbbbabaabbababababaabbabababaabaaabbbbaaaabbbaaaaaabaaabaaaaaaabababbbbaababbaabaaa",
                                        "aabbabbaabbbbaaabaaabbbaababaaaabaaabbabbabbbabaaaaaaabaaabaabaaabbaa",
                                        "bbbbabbbababaababbaababaabbababaaabaabaabbababaaaabbbabaaaabaababaabaabaaababbabbabbbbabaabbaa",
                                        "abbabababaabaabababaabbbaaaabaaaaaabbaaabbaabbaaababbaaaabbbabbabbbbbbaaaabbabbbaabbabbbbbbbaa",
                                        "bababbaaaaaabaabbaaabbbabbaababbabbbbaaabbbbabaababaaabbaaaba",
                                        "bababbbaaaabbbbbbbaababbaabbbababbaaaaaabaaabbabaabbbabbabbbba",
                                        "abbbbabbbbbaabaaabbababbbabababbaabbabbbbbaaaababaabbabaababababbaabababba",
                                        "ababaaabbbbbaaaabababbbababbaababbaaabbabbaaabababaabaabbbaaabaabbbaabababaaaaabbbaabaaabaaababaaba",
                                        "bbbaabbabbaababababbbbaaaabaababaaaababbaaabababbbbbaaaabaaaaaabbaaaabbbbabb",
                                        "bbbabbababbbaaaaabbbababbbabababbbaabbaabbabaaaaaaaaababbbabbbabbabaabaaababaaabbabbabbab",
                                        "aaababababbaabababaabbaabbabbabbaaaaabbabbabbbbbabbbaaababbaabaabaabbbbbababbbaabaaba",
                                        "baaaaaabbbbabbababbaaabbababbbbbbaabbbbaaaabbabbaabaabbbb",
                                        "aaaaabbbaaabbbbbaaabbababaaabbabaaababbbbbabbaaaaabbbbbbaaabbba",
                                        "aaabbbbabaabbabbbabababaabbaaabbababbbbaabbabbabaaabbbaaabaa",
                                        "abbbabaabbbabbbaaaaabbababbaabaabbaabbababaaaaabbaaabbaabaaababaaabbbabbaab",
                                        "abbbaaabbaaabbaaababbababbabbbaaabbaabaaaabbbbabaaaabbba",
                                        "bbaabaaaababbaaabaabbbaaaaababaaaaabaaabbaabbbbabaababbaaaaabbbabaabababbbabbbbaaaaa",
                                        "abaaaabbabbbaababbaabaaaaaaabbabbbbaababaaabbabaabaaaaaaabbbabbbbbbaabaabbabaaabbabbbabbbabaabaaabbb",
                                        "babaaababbaaaababbaabbbbbaabaababbbaabaabababababababbabaabaababbaababaabbabbbbbbaaababaabb",
                                        "bbbaaababbabbbababaaabbaabbbaabababbbabbbbbbbbabaaaaa"])

        with open('stream_checker_test_4_query.json') as f:
            res = json.load(f)

        for i, item in enumerate(res['query']):
            result = stream_checker.query(item[0])
            # expected = res['expected'][i]
            # print('letter: {}, result: {}'.format(item[0], result))
