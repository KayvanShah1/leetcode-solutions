import sys


sys.set_int_max_str_digits(100000)


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = map(str, num)
        num = int("".join(num)) + k
        num = list(str(num))
        num = map(int, num)
        return num
