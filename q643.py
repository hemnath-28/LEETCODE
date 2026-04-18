class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        l=0
        r=k
        n=len(nums)
        fsum=sum(nums[l:r])
        maxsum=float(fsum/k)
        while r<n:
            fsum=fsum-nums[l]+nums[r]
            l+=1
            r+=1
            maxsum=max(float(maxsum),float(fsum/k))
        
        return float(maxsum)
lc=Solution()
nums = [1,12,-5,-6,50,3]
k = 4
ans=lc.findMaxAverage(nums,k)

print(ans)