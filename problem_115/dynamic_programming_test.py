import unittest
from problem_115.dynamic_programming import DynamicProgramingSolution


class MyTestCase(unittest.TestCase):

    def test1(self):
        s = 'rabbbit'
        t = 'rabbit'

        solution = DynamicProgramingSolution()
        result = solution.num_distinct(s, t)
        self.assertEqual(3, result)

    def test2(self):
        s = 'babgbag'
        t = 'bag'

        solution = DynamicProgramingSolution()
        result = solution.num_distinct(s, t)
        self.assertEqual(5, result)

    def test3(self):
        s = 'aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe'
        t = 'bddabdcae'

        solution = DynamicProgramingSolution()
        result = solution.num_distinct(s, t)
        self.assertEqual(10582116, result)

    def test4(self):
        s = 'xslledayhxhadmctrliaxqpokyezcfhzaskeykchkmhpyjipxtsuljkwkovmvelvwxzwieeuqnjozrfwmzsylcwvsthnxujvrkszqwtglewkycikdaiocglwzukwovsghkhyidevhbgffoqkpabthmqihcfxxzdejletqjoxmwftlxfcxgxgvpperwbqvhxgsbbkmphyomtbjzdjhcrcsggleiczpbfjcgtpycpmrjnckslrwduqlccqmgrdhxolfjafmsrfdghnatexyanldrdpxvvgujsztuffoymrfteholgonuaqndinadtumnuhkboyzaqguwqijwxxszngextfcozpetyownmyneehdwqmtpjloztswmzzdzqhuoxrblppqvyvsqhnhryvqsqogpnlqfulurexdtovqpqkfxxnqykgscxaskmksivoazlducanrqxynxlgvwonalpsyddqmaemcrrwvrjmjjnygyebwtqxehrclwsxzylbqexnxjcgspeynlbmetlkacnnbhmaizbadynajpibepbuacggxrqavfnwpcwxbzxfymhjcslghmajrirqzjqxpgtgisfjreqrqabssobbadmtmdknmakdigjqyqcruujlwmfoagrckdwyiglviyyrekjealvvigiesnvuumxgsveadrxlpwetioxibtdjblowblqvzpbrmhupyrdophjxvhgzclidzybajuxllacyhyphssvhcffxonysahvzhzbttyeeyiefhunbokiqrpqfcoxdxvefugapeevdoakxwzykmhbdytjbhigffkmbqmqxsoaiomgmmgwapzdosorcxxhejvgajyzdmzlcntqbapbpofdjtulstuzdrffafedufqwsknumcxbschdybosxkrabyfdejgyozwillcxpcaiehlelczioskqtptzaczobvyojdlyflilvwqgyrqmjaeepydrcchfyftjighntqzoo'
        t = 'rwmimatmhydhbujebqehjprrwfkoebcxxqfktayaaeheys'

        solution = DynamicProgramingSolution()
        result = solution.num_distinct(s, t)
        self.assertEqual(543744000, result)
