class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=len(s)
        l2=len(t)
        pt1=0
        pt2=0
        
        while pt1<l1:
            while pt2<l2 and t[pt2]!=s[pt1]:
                pt2+=1
            if pt2>=l2:
                return False
            if s[pt1]==t[pt2]:
                pt1+=1
            if pt1==l1:
                return True
        return False
            
        
        
        
lc=Solution()
s = "acb"
t = "ahbgdc"
ans=lc.isSubsequence(s,t)
print(ans)