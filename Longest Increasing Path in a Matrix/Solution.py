class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        @lru_cache(None)
        def backtrack(i, j):            
            result = 1
            val = matrix[i][j]
            matrix[i][j] = -1 
			
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not x >= 0 <= y: continue
                if not x < len(matrix): continue
                if not y < len(matrix[0]): continue
                if matrix[x][y] == -1: continue
                if matrix[x][y] <= val: continue
                result = max(result, backtrack(x, y)+1) 
				
            matrix[i][j] = val 
            return result
            
                                                
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(backtrack(i, j), result)
                
                            
        return result
