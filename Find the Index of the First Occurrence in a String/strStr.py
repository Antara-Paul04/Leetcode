class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=="":
            return 0
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i: i+len(needle)]== needle:
                return i
        return -1
solution= Solution()
haystack = "sadbutsad"
needle = "sad"
print(solution.strStr(haystack, needle))
