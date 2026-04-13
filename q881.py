class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boatcount=0
        left=0
        n=len(people)
        right=n-1
        while left<=right:
            if people[left]+people[right]<=limit:
                boatcount+=1
                left+=1
                right-=1
            elif people[left]+people[right]>limit:
                boatcount+=1
                right-=1
                
        print(boatcount)
        return boatcount
lc=Solution()
nums = [3,5,3,4]

ans=lc.numRescueBoats(nums,5)