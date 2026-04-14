class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        minvalue=float('inf')
        output=0
        for k in range(n):
            left=k+1
            right=n-1
            while left<right:
                result=nums[k]+nums[left]+nums[right]
                check=abs(target-result)
                if check<minvalue:
                    minvalue=check
                    output=result
                if (result)<target:
                    left+=1
                else:
                    right-=1
        return output
                
                
lc=Solution()
nums=[-1,2,1,-4]
lc.threeSumClosest(nums,1)
                
                
            