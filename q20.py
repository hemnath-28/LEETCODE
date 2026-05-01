class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        stack=[]
        hashmap={']':'[',')':'(','}':'{'}
        for i in range(n):
            if not stack:
                stack.append(s[i])
                continue
            else:
                pair=hashmap.get(s[i],0)
                if stack[-1]==pair:
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)==0

            
              