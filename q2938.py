class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """

        # s="101"
        n=len(s)
        low=0
        high=n-1
        count=0
        while low<high:
            if s[low]=="1":
                while low<high and s[high]=="1":
                    high-=1
                count+=(high-low)
                high-=1
            low+=1
        return count
        
        
        
lc=Solution()
s="111000"
ans=lc.minimumSteps(s)
            
        