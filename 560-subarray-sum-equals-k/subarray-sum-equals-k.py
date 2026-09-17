class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        mp = {0: 1} 
        sum1 = 0
        count = 0
        
        for i in nums:
            sum1 += i
            
            if (sum1 - k) in mp:
                count += mp[sum1 - k]

            mp[sum1] = mp.get(sum1, 0) + 1
            
        return count

        
