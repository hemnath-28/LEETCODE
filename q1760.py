class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        import math
        n=len(nums)
        totalballs=n+maxOperations
        def feasible(value):
            cnt=0
            accsum=0
            for i in range(n):
                if nums[i]//value==0:
                    accsum+=1
                else:
                    accsum+=math.ceil(nums[i]/value)
            return accsum
        low=1
        high=max(nums)
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            feasvalue=feasible(mid)
            if feasvalue<=totalballs:
                high=mid-1  
            else:
                low=mid+1
               
        print(low,mid,high,ans)
        return low
lc=Solution()
nums = [9]
maxOperations = 1
ans=lc.minimumSize(nums,maxOperations)
print(ans)