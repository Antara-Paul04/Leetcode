class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, len(charSet))

        return res

# Example usage:
solution = Solution()
s = "abcabcbb"
result = solution.lengthOfLongestSubstring(s)
print(result)
