class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        suffix=[0]*51
        hashtable={}
        n=len(nums)
        for i in range(k):
            if nums[i] not in hashtable:
                hashtable[nums[i]]=1
                suffix[nums[i]]=nums[i]
            else:
                hashtable[nums[i]]+=1
                suffix[nums[i]]+=nums[i]
        print(sorted(suffix))
        print(hashtable)
lc=Solution()
nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
ans=lc.findXSum(nums,k,x)
print(ans)