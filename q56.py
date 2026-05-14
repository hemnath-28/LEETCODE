class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        n=len(intervals)
        intervals=sorted(intervals)
        output=[]
        for i in range(n):
            if i==0:
                output.append(intervals[0])
            else:
                if output[-1][1]>=intervals[i][0]:
                    output[-1][1]=max(output[-1][1],intervals[i][1])
                else:
                    output.append(intervals[i])
       
        return output
            
                
        