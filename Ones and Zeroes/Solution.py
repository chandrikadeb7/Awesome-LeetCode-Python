class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [Counter(s) for s in strs]
        @lru_cache(None)
        
        def func(i, a, b):
            if a > m or b > n:
                return -1
            if i == len(strs):
                return 0
            x = func(i + 1, a + count[i]['0'], b + count[i]['1'])
            if x != -1:
                return max(1 + x, func(i + 1, a, b))
            return func(i + 1, a, b)
        return func(0, 0, 0)
