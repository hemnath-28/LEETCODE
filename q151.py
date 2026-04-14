class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip().split()
        n=len(s)
        left=0
        right=n-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        
        return " ".join(s)
        
        
        
s = "  the sky is blue"
lc=Solution()
ans=lc.reverseWords(s)
print(ans)
