class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        hashtable={}
        n1=len(list1)
        for i in range(n1):
            hashtable[list1[i]]=i
        n2=len(list2)
        output=[]
        minidx=9999
        for i in range(n2):
            data=list2[i]
            if data in hashtable:
                idx=i+hashtable[data]
                if idx<minidx:
                    output=[]
                    output.append(data)
                    minidx=idx
                elif idx==minidx:
                    output.append(data)
        return output



        