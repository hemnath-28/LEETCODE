class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l=0
        r=0
        hashmap={}
        n=len(s)
        maxlen=0
        while r<n:
            if s[r] not in hashmap:
                hashmap[s[r]]=1
            else:
                while s[r]  in hashmap:
                    del hashmap[s[l]]
                    l+=1
                hashmap[s[r]]=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
        
            
            
s = "abcabcbb"        
lc=Solution()
ans=lc.lengthOfLongestSubstring(s)
print(ans)