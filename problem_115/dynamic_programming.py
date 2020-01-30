from problem_115.solution import Solution


# 动态规划法
class DynamicProgramingSolution(Solution):

    def num_distinct(self, s: str, t: str) -> int:
        dpx = len(s) + 1
        dpy = len(t) + 1

        dp = [[0] * dpx for _ in range(dpy)]

        for x in range(dpx):
            dp[0][x] = 1

        for y in range(1, dpy):
            for x in range(1, dpx):
                if t[y - 1] == s[x - 1]:
                    dp[y][x] = dp[y - 1][x - 1] + dp[y][x - 1]
                else:
                    dp[y][x] = dp[y][x - 1]
        return dp[-1][-1]
