class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)
        left=0
        right=n-1
        while left<right:
            temp=s[left]
            s[left]=s[right]
            s[right]=temp
            left+=1
            right-=1
        print(s)

s = ["h","e","l","l","o"]
lc=Solution()
lc.reverseString(s)
        