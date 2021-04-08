class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
        result = [''] if digits else []
        for d in digits:
            result = [p + q for p in result for q in map[d]]
        return result
