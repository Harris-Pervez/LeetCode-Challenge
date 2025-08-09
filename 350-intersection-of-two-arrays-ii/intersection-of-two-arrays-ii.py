class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new=[]
        if len(nums1)<=len(nums2):
            for i in nums1:
                if i in nums2:
                    new.append(i)
                    nums2.pop(nums2.index(i))
        elif len(nums1)>=len(nums2):
            for i in nums2:
                if i in nums1:
                    new.append(i)
                    nums1.pop(nums1.index(i))
        
        return new