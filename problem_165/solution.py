class Solution:

    def compare_version(self, version1: str, version2: str) -> int:
        split1 = version1.split('.')
        split2 = version2.split('.')

        short, long, is_reversed = (split1, split2, False) if len(split1) < len(split2) else (split2, split1, True)

        result = self._compare(short, long)

        return -result if is_reversed else result

    def _compare(self, short: list, long: list) -> int:
        short_len = len(short)
        for i, s in enumerate(long):
            num2 = int(s)
            if i < short_len:
                num1 = int(short[i])
                if num1 < num2:
                    return -1
                if num1 > num2:
                    return 1
            else:
                if num2 > 0:
                    return -1
        return 0
