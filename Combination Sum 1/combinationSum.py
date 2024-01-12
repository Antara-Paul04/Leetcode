class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(list(cur))  # Change this line
                return
            if total > target or i >= len(candidates):
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

solution = Solution()
candidates = [2, 3, 6, 7]
target = 7
result = solution.combinationSum(candidates, target)
print(result)
