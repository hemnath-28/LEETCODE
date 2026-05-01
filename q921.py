class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        stack=[]
        
        for i in range(n):
            if s[i]=='(':
                stack.append(s[i])
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)