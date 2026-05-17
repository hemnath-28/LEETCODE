class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap={0:1}
        n=len(nums)
        accsum=0
        cnt=0
        for i in range(n):
            accsum+=nums[i]
            find=accsum-k
           
            if find in hashmap:
                cnt+=hashmap.get(find)
            hashmap[accsum]=hashmap.get(accsum,0)+1
        return cnt
lc=Solution()
nums =[-1,-1,1]
k=0
ans=lc.subarraySum(nums,k)
print(ans)