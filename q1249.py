class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        n=len(s)
        output=[]
        cnt=0
        for i in range(n):
            if s[i]=="(":
                stack.append(s[i])
                cnt+=1
            elif s[i]==")" and cnt>0:
                stack.append(s[i])
                cnt-=1
            elif s[i]!=")":
                stack.append(s[i])
        for i in stack[::-1]:
            if i==")" and cnt>0:
                cnt-=1
            else:
                output.append(i)
        return "".join(output[::-1])
        
        
lc=Solution()
s="a)b(c)d"
ans=lc.minRemoveToMakeValid(s)
print(ans)