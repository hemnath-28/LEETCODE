class Solution:
    def shipWithinDays(self, weights, days):

        import math
        n=len(weights)
        def possible(weights,value):
            accumsum=0
            accdays=0
            for i in range(n):
                accumsum+=weights[i]
                if accumsum>value:
                    accdays+=1
                    accumsum=weights[i]
            return accdays+1
        
        left=max(weights)
        right=sum(weights)
        
        while left<right:
            mid=left+(right-left)//2
            funcdays=possible(weights,mid)
            if funcdays<=days:
                # if funcdays<days value is high so we need to reduce it
                right=mid
            else:
                left=mid+1
        return left

lc=Solution()
weights = [3,2,2,4,1,4]
days = 3
ans=lc.shipWithinDays(weights,days)
print(ans)