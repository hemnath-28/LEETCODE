class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=0
        n=len(nums)
        zero=0
        maxlen=0
        while end<n:
            if nums[end]==0:
                zero+=1
            while zero>1:
                if nums[start]==0:
                    zero-=1
                start+=1
                
            maxlen=max(maxlen,end-start)
            end+=1
        return maxlen
        
        
lc=Solution()
nums=[0,1,1,1,0,1,1,0,1]
ans=lc.longestSubarray(nums)
print(ans)