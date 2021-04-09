class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        myDict = {}
        k = ord('a')
        for i in order:
            myDict[i] = chr(k)
            k += 1
        prev = ""
        for word in words:
            cur = ""
            for c in word:
                cur += myDict[c]      
            if cur < prev:            
                return False
            prev = cur             
        return True
