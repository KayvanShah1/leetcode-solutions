class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Creating an empty array for largest trip possible
        trip_length = [0]*1001
        
        for numPassengers, pickup, drop in trips:
            # Picking up passengers from their pickup location
            trip_length[pickup] += numPassengers
            
            # Dropping passengers at their drop location
            trip_length[drop] -= numPassengers
        
        # Check the capacity of car at every location
        for num_pass in trip_length:
            capacity -= num_pass
            
            if capacity < 0:
                return False
            
        return True