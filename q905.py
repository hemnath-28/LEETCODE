class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n=len(nums)
        ptreven=0
        ptrodd=n-1
        while ptreven<ptrodd:
            if nums[ptreven]%2==1:
                while ptrodd>=0 and nums[ptrodd]%2==1:
                    ptrodd-=1
                nums[ptrodd],nums[ptreven]=nums[ptreven],nums[ptrodd]
                ptrodd-=1
            ptreven+=1
        print(nums)
            
                








nums = [0,1,3]
lc=Solution()
ans=lc.sortArrayByParity(nums)