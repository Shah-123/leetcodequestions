class Solution(object):
    def singleNumber(self,nums):
        for i in nums:
            if nums.count(i) == 1:
                return i 
nums = [4,1,2,1,2]
solution = Solution()
print(solution.singleNumber(nums))