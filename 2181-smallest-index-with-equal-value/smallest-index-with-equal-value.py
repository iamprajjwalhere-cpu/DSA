class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i % 10 == nums[i]:
                return i
            
        return -1

        