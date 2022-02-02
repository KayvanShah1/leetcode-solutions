class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        h = 0
        
        while start < end:
            if height[start] < height[end]:
                h = height[start]
                start += 1
            else:
                h = height[end]
                end -= 1
            area = h*(end-start+1)
            max_area = max(max_area, area)
        return max_area