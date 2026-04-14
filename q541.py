class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=list(s)
        n=len(s)
        rev=True
        temp=""
        for i in range(0,n,2):
            if rev:
                temp+="".join(s[i:i+2][::-1])
                rev=False
            else:
                temp+="".join(s[i:i+2])
                rev=True
        print(temp)
            
            
            

s ="abcdefg"
lc=Solution()
ans=lc.reverseStr(s,2)
print(ans)