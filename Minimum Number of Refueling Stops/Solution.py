class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)  # Initialize dp

        for i, (loc, cap) in enumerate(stations):  # Traversing the gas station
            for t in range(i, -1, -1):
                if dp[t] >= loc:  # If the t fuel, can reach the position of the current gas station.
                    dp[t+1] = max(dp[t+1], dp[t] + cap)  # Attempt to update dp

        for i, d in enumerate(dp):  # Traversing a minimum number of times
            if d >= target: return i
        return -1
        
