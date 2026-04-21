class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        start=0
        end=0
        n=len(fruits)
        hashmap={}
        maxlen=0
        while end<n:
            hashmap[fruits[end]]=hashmap.get(fruits[end],0)+1
            hashlen=len(hashmap)
            while hashlen>2:
                hashmap[fruits[start]]-=1
                if hashmap[fruits[start]]==0:
                    hashlen-=1
                    del hashmap[fruits[start]]
                start+=1
            
            maxlen=max(maxlen,end-start+1)
            end+=1
        return maxlen
    
lc=Solution()
fruits = [1,2,3,2,2]
ans=lc.totalFruit(fruits)
print(ans)