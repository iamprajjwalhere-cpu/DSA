class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        i = 0
        while i <= len(nums) - 1:
            if nums[i] in seen:
                return True

            seen[nums[i]] = True
            i += 1

        return False

        