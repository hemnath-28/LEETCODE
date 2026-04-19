class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        n1=len(s1)
        n2=len(s2)
        first={}
        main={}
        for i in range(n1):
            first[s1[i]]=first.get(s1[i],0)+1
            main[s2[i]]=main.get(s2[i],0)+1
        if first==main:
            return True
        l=0
        r=n1
        while r<n2:
            if s2[l] in main:
                main[s2[l]]-=1
            if main[s2[l]]==0:
                del main[s2[l]]
            main[s2[r]]=main.get(s2[r],0)+1
            if main==first:
                return True
            l+=1
            r+=1
        return False
lc=Solution()
s1 = "ab"
s2 = "eidbaooo"
ans=lc.checkInclusion(s1,s2)
print(ans)