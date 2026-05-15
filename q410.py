class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left=max(nums)
        right=sum(nums)
        n=len(nums)
        def feasible(value):
            data=0
            count=1
            for i in range(n):
                data+=nums[i]
                if data>value:
                    count+=1
                    data=nums[i]
            return count                
        while left<=right:
            mid=left+(right-left)//2
            funcval=feasible(mid)
            if funcval<=k:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        print(left,mid,right)
        return ans
    
lc=Solution()
nums = [7,2,5,10,8]
k = 3
ans=lc.splitArray(nums,k)
print(ans)