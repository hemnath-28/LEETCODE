class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=0
        r=k-1
        n=len(nums)
        output=[]
        while r<n:
            idx=r
            if output and output[-1]!=-1:
                if nums[idx]==nums[idx-1]+1:
                    idx=l
            else:
                while idx>l and nums[idx]==nums[idx-1]+1:
                    idx-=1

            if idx==l:
                output.append(nums[r])
            else:
                output.append(-1)
            l+=1
            r+=1
        return output
lc=Solution()
nums = [1,2,3,4,3,2,5]
k=3
ans=lc.resultsArray(nums,k)
print(ans)