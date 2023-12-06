class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    res_l = l
                    res_r = r
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    res_l = l
                    res_r = r
                l -= 1
                r += 1

        return s[res_l : res_r + 1]

solution = Solution()
s = "babad"
result = solution.longestPalindrome(s)
print(result)

