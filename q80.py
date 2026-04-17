class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        tempcount=0
        read=0
        write=0
        n=len(nums)
        while read<n:
            if read==0:
                nums[write]=nums[read]
                read+=1
                write+=1
                tempcount+=1
            elif nums[read]==nums[read-1]:
                tempcount+=1
                if tempcount<=2:
                    nums[write]=nums[read]
                    read+=1
                    write+=1
                elif tempcount>2:
                    while nums[read]==nums[read-1]:
                        read+=1
                    tempcount=0
            else:
                tempcount=0
                nums[write]=nums[read]
                read+=1
                write+=1
                tempcount+=1
                
        print(write)
        print(nums)
        
nums=[1,1,1,2,2,3]
lc=Solution()
ans=lc.removeDuplicates(nums)
        
            
        