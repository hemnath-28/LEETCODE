class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start=0
        ptr=0
        n=len(nums)
        while start<n:
            
            start+=1
            ptr+=1
            while start!=0 and start<n and nums[start]==nums[start-1]:
                start+=1
            nums[ptr]=nums[start]
        return ptr
lc=Solution()
nums= [0,0,1,1,1,2,2,3,3,4]
ans=lc.removeDuplicates(nums)
print(ans)