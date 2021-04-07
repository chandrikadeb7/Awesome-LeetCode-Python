class Solution:
    def countVowel(self, s):
        count = 0
        for ch in s:
            if ch=='a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
                count = count + 1
            else:
                continue
        return count    
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        n = l//2
        s1 = s[:n]
        s2 = s[n:]
        
        m = self.countVowel(s1)
        n = self.countVowel(s2)
        
        if m==n:
            return True
        else:
            return False
