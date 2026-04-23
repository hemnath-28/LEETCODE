class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start=end=total=0
        prod=1
        n=len(nums)
        if k<=1:
            return 0
        while end<n:
            prod*=nums[end]
            while prod>=k:
                prod//=nums[start]
                start+=1
                
            total+=(end-start+1)
            end+=1
        return total



lc=Solution()
nums = [10,5,2,6]
k = 100
ans=lc.numSubarrayProductLessThanK(nums,k)
print(ans)