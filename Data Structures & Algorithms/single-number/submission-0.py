class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        extra = 0
        for i in range(len(nums)):
            extra = extra ^ nums[i]
        return extra