class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        Split_word = s.split()
        return len(Split_word[-1])
    
    
    
    
s = "catch me if you can"
solution = Solution()
print(solution.lengthOfLastWord(s))