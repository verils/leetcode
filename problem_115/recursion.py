from problem_115.solution import Solution


# 递归法
class RecursionSolution(Solution):
    def num_distinct(self, s: str, t: str) -> int:
        return self._num_distinct(s, 0, t, 0, {})

    def _num_distinct(self, s: str, s_offset: int, t: str, t_offset: int, cache: dict) -> int:
        key = '{}.{}'.format(s_offset, t_offset)

        cached = cache.get(key)
        if cached is not None:
            return cached
        if cached == 0:
            return 0

        if t_offset == len(t):
            return 1
        if s_offset == len(s):
            return 0

        s_start = s.find(t[t_offset], s_offset)
        if s_start == -1:
            cache[key] = 0
            return 0
        else:
            count = self._num_distinct(s, s_start + 1, t, t_offset + 1, cache) + \
                    self._num_distinct(s, s_start + 1, t, t_offset, cache)
            cache[key] = count
            return count
