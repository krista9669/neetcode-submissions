class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()
        for i in range(len(nums)):
            if nums[i] in sett:
                return nums[i]
            sett.add(nums[i])