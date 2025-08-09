class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L=nums1+nums2
        new=[]
        for i in L:
            if i in nums1 and i in nums2 and i not in new:
                new.append(i)
        return new
        