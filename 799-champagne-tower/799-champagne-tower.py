class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass = [[0] * k for k in iter(range(1 , 102))]
        glass[0][0] = poured
        
        for row in iter(range(query_row + 1)):
            for col in iter(range(row + 1)):
                quantity = (glass[row][col] - 1.0) / 2.0
                if quantity > 0:
                    glass[row + 1][col] += quantity
                    glass[row + 1][col + 1] += quantity   
                    
        return min(1, glass[query_row][query_glass])

        
        