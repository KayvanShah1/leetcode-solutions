import math


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return ((2 << int(math.log(max(n, 1), 2))) - 1) - n