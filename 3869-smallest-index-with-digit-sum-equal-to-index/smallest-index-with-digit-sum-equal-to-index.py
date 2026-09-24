class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            digit_sum = sum(int(d) for d in str(val))
            if i == digit_sum:
                return i
            
        return -1
        