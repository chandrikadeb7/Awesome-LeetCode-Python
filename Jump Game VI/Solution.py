class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        pq = [(0, -k)]
        for i, a in enumerate(nums):
            while i - pq[0][1] > k: heappop(pq)
            a -= pq[0][0]
            heappush(pq, (-a, i))
        return a
