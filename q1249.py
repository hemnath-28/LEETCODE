class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        n=len(s)
        for i in range(n):
            if s[i]=="(":
                stack.append((s[i],i))
            elif s[i]==")":
                if stack and stack[-1][0]=="(":
                    stack.pop()
                else:
                    stack.append((s[i],i))
        hset=set()
        for k in range(len(stack)):
            hset.add(stack[k][1])
        output=""
        for i in range(n):
            if i not in hset:
                output+=s[i]
        print(output)
        
lc=Solution()
s="a)b(c)d"
ans=lc.minRemoveToMakeValid(s)
print(ans)