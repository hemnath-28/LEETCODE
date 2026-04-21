class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start=0
        end=0
        n=len(s)
        hashmap={}
        maxlen=0
        maxf=float('-inf')
        while end<n:
            if s[end] not in hashmap:
                hashmap[s[end]]=1
            else:
                hashmap[s[end]]+=1
            maxf = max(maxf,hashmap[s[end]])
            while (end - start + 1) - maxf > k:
                
                hashmap[s[start]]-=1
                if hashmap[s[start]]==0:
                    del hashmap[s[start]]
                start+=1
            maxlen=max(maxlen,end-start+1)
            end+=1
        return maxlen
lc=Solution()
s = "AABABBA"
k = 1
ans=lc.characterReplacement(s,k)
print(ans)