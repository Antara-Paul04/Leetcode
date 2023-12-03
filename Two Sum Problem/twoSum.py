class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices={}
        for i, num in enumerate(nums):
            complement= target-num
            if complement in num_indices:
                return [num_indices[complement], i]
            else:
                num_indices[num]=i
        return []

solution=Solution()
nums=[2,7,11,15]
target=9
result= solution.twoSum(nums, target)
print result
