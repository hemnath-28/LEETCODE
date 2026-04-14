class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        output=set()
        for o in range(n):
            if o > 0 and nums[o] == nums[o-1]:
                continue
            for i in range(o+1,n):
                if i > o+1 and nums[i] == nums[i-1]:
                    continue
                left=i+1
                right=n-1
                while left<right:
                    result=nums[left]+nums[right]+nums[o]+nums[i]
                    if result==target:
                        output.add((nums[o],nums[i],nums[left],nums[right]))
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
            
                    elif result<target:
                        left+=1
                    else:
                        right-=1
        return [list(item) for item in output]
                       
        
lc=Solution()
nums = [2,2,2,2,2]
target = 8
ans=lc.fourSum(nums,target)
print(ans)
                    
                    
                        
                    
                    