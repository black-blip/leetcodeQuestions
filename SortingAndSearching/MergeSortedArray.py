class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j = m-1,n-1
        
        for term in range(n+m-1,-1,-1):
            
            if j<0:
                break
            
            if i>=0 and nums1[i]>nums2[j]:
                nums1[term] = nums1[i]
                i-=1
            else:
                nums1[term] = nums2[j]
                j-=1
            
