class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for x in sorted(nums,reverse = True):
            if -1*x in nums:
                return x
        return -1
