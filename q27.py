class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start=0
        ptr=0
        n=len(nums)
        while start<n:
            while start<n and nums[start]==val:
                start+=1
            if start<n:
                nums[ptr]=nums[start]
                ptr+=1
                start+=1
        return ptr

lc=Solution()
nums= [0,1,2,2,3,0,4,2]
ans=lc.removeElement(nums,2)
print(ans)