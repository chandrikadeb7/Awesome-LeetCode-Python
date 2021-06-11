class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        dpCurr, dpLast = [0] * N, [0] * N
        for i in range(N - 2, -1, -1):
            total = stones[i]
            dpLast, dpCurr = dpCurr, dpLast
            for j in range(i + 1, N):
                total += stones[j]
                dpCurr[j] = max(total - stones[i] - dpLast[j], total - stones[j] - dpCurr[j-1])
        return dpCurr[-1]
