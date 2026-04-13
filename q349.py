class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        
        ptr1=0
        n1=len(nums1)
        n2=len(nums2)
        ptr2=0
        output=[]
        while ptr1<n1 and ptr2<n2:
            if nums1[ptr1]==nums2[ptr2]:
                output.append(nums1[ptr1])
                ptr2+=1
                ptr1+=1
                while ptr1<n1 and nums1[ptr1]==nums1[ptr1-1]:
                    ptr1+=1
                while ptr2<n2 and nums2[ptr2]==nums2[ptr2-1]:
                    ptr2+=1
            elif nums1[ptr1]>nums2[ptr2]:
                ptr2+=1
                while ptr2<n2 and nums2[ptr2]==nums2[ptr2-1]:
                    ptr2+=1
            else:
                ptr1+=1
                while ptr1<n1 and nums1[ptr1]==nums1[ptr1-1]:
                    ptr1+=1
        print(output)
        return output
lc=Solution()
nums1 = [4,9,5]
nums2 =[9,4,9,8,4]
ans=lc.intersection(nums1,nums2)
print(ans)
                