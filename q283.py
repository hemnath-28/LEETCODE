class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        start=0
        ptr=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                
                for start in range(i+1,n):
                    if nums[start]>0:
                        nums[start],nums[i]=nums[i],nums[start]
                        break
        print(nums)

lc=Solution()
nums = [0,1,0,3,12]
ans=lc.moveZeroes(nums)
print(ans)