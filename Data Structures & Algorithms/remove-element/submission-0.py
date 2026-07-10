class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        ans = []
        for i in range(len(nums)):
            if nums[i] != val:
                ans.append(nums[i])
        k = len(ans)
        nums[:k] = ans
        return k