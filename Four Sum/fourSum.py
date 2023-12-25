class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res, quad = [], []

        def ksum(k, start, target):
            if k == 2:  # Corrected this line
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])  # Corrected this line
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    ksum(k - 1, i + 1, target - nums[i])
                    quad.pop()

        ksum(4, 0, target)
        return res

sol = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = sol.fourSum(nums, target)
print(result)
