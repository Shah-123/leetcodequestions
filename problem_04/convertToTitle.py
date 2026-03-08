

class Solution(object):
    def convertToTitle(self, columnNumber):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        columnNumber= 100
    
        while columnNumber > 0:
                columnNumber -= 1
                remainder = columnNumber % 26
                result = letters[remainder] + result 
        
        return result
    
solution = Solution()   
print(solution.convertToTitle(100))