class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        n=len(nums)
        for i in range(n):
            check=target-nums[i]
            if check in hashmap:
                return [i,hashmap[check]]
            else:
                hashmap[nums[i]]=i
        
        
            