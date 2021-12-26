class Solution:
    def euclidean_distance(self, point: List[int]):
        return point[0]**2 + point[1]**2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.euclidean_distance)
        return points[:k]