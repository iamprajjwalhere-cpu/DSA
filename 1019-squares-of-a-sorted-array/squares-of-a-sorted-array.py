class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0]*len(nums)
        p,q,k = 0,len(nums)-1,len(nums)-1
        while k>=0:
            if abs(nums[p])>abs(nums[q]):
                res[k],p=nums[p]**2,p+1
            else:
                res[k],q  = nums[q]**2,q-1
            k-=1
            
        return res