class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c=0
        while True:
            for i in range(c+1,len(nums)):
                if nums[c]+nums[i]==target:
                    return [c,i]
            c+=1

    
        