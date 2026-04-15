class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        idx=n-1
        temp=""
        count=0
        while idx>=0:
            while s[idx]=="*":
                count+=1
                idx-=1
            if count>0:
                idx=idx-count
                count=0
            else:
                temp+=s[idx]
                idx-=1
        print(temp[::-1])
lc=Solution()
s = "abb*cdfg*****x*"
ans=lc.removeStars(s)
print(ans)