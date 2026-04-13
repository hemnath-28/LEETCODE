class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        # [1,8,6,2,5,4,8,3,7]
        left=0
        right=n-1
        maxarea=0
        while left<n:
            h=min(height[left],height[right])
            w=right-left
            area=h*w
            
            maxarea=max(h*w,maxarea)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
                
                
        return maxarea
lc=Solution()
nums=[8,7,2,1]
result=lc.maxArea(nums)
print(result)
            