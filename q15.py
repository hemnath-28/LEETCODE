class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [-1,0,1,2,-1,-4]
        nums.sort()
        #[-1,-1,0,1,2,-4]
        n=len(nums)
        output=[]
        for k in range(n):
            if k!=0 and nums[k-1]==nums[k]:
                continue
            
            left=k+1
            right=n-1
            while left<right:
                
                result=nums[k]+nums[left]+nums[right]
                if result==0:
                    output.append([nums[k],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left-1]==nums[left]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1    
                elif result<0:
                    left+=1
                else:
                    right-=1
                
        print(output)
        return output
                
                
                              
lc=Solution()
nums=[-1,0,1,2,-1,-4]
nums2=[0,1,1]
nums3=[0,0,0,0]
res=lc.threeSum([1,2,0,1,0,0,0,0])

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result_set = set()

        for k in range(n):
            target = -nums[k]
            hashmap = {}

            for i in range(k + 1, n):
                check = target - nums[i]

                if check in hashmap:
                    triplet = [nums[k], nums[i], check]
                    triplet.sort()  
                    result_set.add(tuple(triplet)) 
                else:
                    hashmap[nums[i]] = i

        return [list(t) for t in result_set]