class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        left=1  #min one condies to each childer
        right=max(candies) #mac cnadies may each child get
        n=len(candies)
        if n==1 and k==1:
            return candies[0]
        # [1,2,3,4,5,6,7,8]
        import math
        def satisfy(maxcandy):
            totalpairs=0
            for i in range(n):
                t=candies[i]//maxcandy
                totalpairs+=t
            # print(totalpairs,maxcandy)
            return totalpairs
        fmax=0
        while left<=right:
            mid=left+(right-left)//2
            value=satisfy(mid)
            if value>=k:
                left=mid+1
                fmax=max(fmax,mid)
                
            elif value<k:
                right=mid-1
        # print(left,mid,right)
        return fmax



lc=Solution()
candies = [5,8,6]
k = 6
ans=lc.maximumCandies(candies,k)
print(ans)