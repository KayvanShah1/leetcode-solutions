class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap, total, count = defaultdict(int), 0, 0
        for num in nums:
            total += num
            count += (total == k) + hashmap[total-k]
            hashmap[total] += 1
        return count