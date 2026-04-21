class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap={}
        n=len(nums)
        s=0
        e=0
        while e<n:
            if nums[e] not in hashmap:
                hashmap[nums[e]]=1
            else:
                if s-e+1<=k:
                    return True
                else:
                    hashmap[nums[e]]+=1
            while e-s>=k:
                hashmap[nums[s]]-=1
                if hashmap[nums[s]]==0:
                    del hashmap[nums[s]]
                if nums[e] in hashmap:
                    return True
                else:
                    hashmap[nums[e]]=1
                    s-=1
            e+=1

lc=Solution()
nums = [1,2,3,1]
k = 3
ans=lc.containsNearbyDuplicate(nums,k)
print(ans)