class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start=0
        end=0
        n=len(nums)
        ones=0
        maxlen=0
        while end<n:
            if nums[end]==1:
                ones+=1
            while end-start+1-ones>k:
                if nums[start]==1:
                    ones-=1
                start+=1
            maxlen=max(maxlen,end-start+1)
            end+=1
        return maxlen










# class Solution(object):
#     def longestOnes(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         start=0
#         end=0
#         hashmap={}
#         maxlen=0
#         maxf=0
#         n=len(nums)
#         while end<n:            
#             hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
#             maxf=max(maxf,hashmap[nums[end]])
            
#             while end-start+1-maxf>k:
#                 hashmap[nums[start]]-=1
#                 start+=1
#             maxlen=max(maxlen,end-start+1)
#             end+=1
#         return maxlen
    
lc=Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans=lc.longestOnes(nums,k)
print(ans)