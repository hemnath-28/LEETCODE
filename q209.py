class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s=0
        e=0
        # target = 7, nums = [2,3,1,2,4,3]
        n=len(nums)
        fsum=0
        minlen=float('inf')
        while e<n:
            fsum+=nums[e]
            while fsum>=target:
                minlen=min(minlen,e-s+1)
                fsum-=nums[s]
                s+=1
               
                
            e+=1
        return minlen
            
                
            
           
        
        
    
lc=Solution()
target = 7
nums = [2,3,1,2,4,3]
nums=[1,4,4]
target=4
ans=lc.minSubArrayLen(target,nums)
print(ans)