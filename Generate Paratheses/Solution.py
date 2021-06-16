class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []              
        res = [[] for _ in range(n+1)]
        res[0] = ['']
        for i in range(1, n+1):
            for j in range(i):
                p = res[j]
                q = res[i-j-1]
                for k1 in p:
                    for k2 in q:
                        res[i].append('(' + k1 +')' + k2)
        return res[n]
