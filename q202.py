class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        def getnext(n):
            n=str(n)
            total=0
            for i in range(len(n)):
                total+=int(n[i])**2
            return total
        slow=getnext(n)
        fast=getnext(getnext(n))
        while fast!=1:
            fast=getnext(getnext(fast))
            slow=getnext(slow)
            
            if slow==fast:
                return False
        return True
            
        
            
                
                
            

lc=Solution()
ans=lc.isHappy(2)
print(ans)
            