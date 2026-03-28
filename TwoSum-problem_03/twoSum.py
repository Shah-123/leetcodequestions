class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target = 8 

        for i in range (0, len(nums)):
            for  j in range (i+1 , len(nums)):
                twosum = nums[i]+nums[j] 
                if twosum == target :
                    return i, j
                else :
                    pass