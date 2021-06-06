class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sum = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                j = i+1
                while j in nums:
                    j+=1
                sum = max(sum, j-i)
        return sum
