class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        head, tail = 0, len(people) - 1
        num_boats = 0
        
        while head <= tail:
            num_boats += 1
            if people[head] + people[tail] <= limit:
                head += 1
            tail -= 1
        return num_boats
                