class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n=len(chars)
        
        ptr=0
        write=0
        while ptr<n:
            count=0
            start=chars[ptr]
            while ptr<n and start==chars[ptr]:
                count+=1
                ptr+=1
            
            if count>1:
                chars[write]=start
                write+=1
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            else:
                chars[write]=start
                write+=1
            if ptr>=n:
                break
            
       
        return write
                
lc=Solution()
chars =["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ans=lc.compress(chars)