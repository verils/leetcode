class Solution:

    def count_vowel_permutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(1, n):
            a_n = e % mod
            e_n = (a + i) % mod
            i_n = (a + e + o + u) % mod
            o_n = (i + u) % mod
            u_n = a % mod
            a, e, i, o, u = a_n, e_n, i_n, o_n, u_n
        return (a + e + i + o + u) % mod
