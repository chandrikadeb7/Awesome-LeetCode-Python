class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = range(1, n+1)
        for i in range(2, k+1): res = res[:i-1] + res[i-1:][::-1]
        return res
