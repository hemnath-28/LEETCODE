class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        fmax=0
        hashmap={}
        accsum=0
        zeros=0
        for i in range(n):
            accsum+=nums[i]
            hashmap[accsum]=i
            if nums[i]==0:
                zeros+=1
                prefix=hashmap.get(accsum-zeros,0)
                fmax=max(fmax,i-prefix)
            else:
                zeros=0
        print(hashmap)
        return fmax
        
lc=Solution()
nums=[0,0,0,1,1,1,0,0,1,1]
ans=lc.findMaxLength(nums)
print(ans)