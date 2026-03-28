class Solution(object):
    def reverseString(self, s):
        y = []
        for i in range (len(s)-1, -1, -1):
            y.append(s[i])
        return y
s = ["H","a","n","n","a","h"]
solution = Solution()
print(solution.reverseString(s))