class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n = len(A)
        g = local = 0
        for i in range(1, n):
            if A[i] < A[i-1]:                  
                local += 1
            if A[i] < i:                        
                diff = i - A[i]                
                g += diff * (diff+1) // 2       
        return g == local
