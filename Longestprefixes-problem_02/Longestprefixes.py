class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] #assume that the first is the string is the longest prefix 
        for i in strs[1:] :
            while not i.startswith(prefix):
                #if the second string not start with prefix then reduce the prefix 
                prefix = prefix[:-1]
                if prefix =="":
                    return ""
        return prefix



solution = Solution()

print (solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix())
