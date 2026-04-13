class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import math
        
        n=len(nums)
        left=0
        right=n-1
        newarray=[0]*n
        print(newarray)
        index=n-1
        while left<=right:
            if abs(nums[left])>nums[right]:
                newarray[index]=nums[left]**2
                left+=1
                
            else:
                newarray[index]=nums[right]**2
                right-=1
            index-=1
        print(newarray)
        return 0
lc=Solution()
nums=[-7,-3,2,3,11]
ans=lc.sortedSquares(nums)

                
                
            