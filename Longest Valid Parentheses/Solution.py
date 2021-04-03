class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.count(s)
    
    def count(self, s):
        s = s.replace("()", "*")
        for i in range(1, len(s)):
            s = s.replace(f"(" + i * "*" + ")", (i + 1) * "*")
        s = s.replace(")", "(")
        s = s.split("(")
        return max(len(p) for p in s) * 2
