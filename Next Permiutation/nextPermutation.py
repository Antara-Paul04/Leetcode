class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind=-1
        n=len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i]< nums[i+1]:
                ind=i
                break

        if ind == -1:
            nums.reverse()
            return
        
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[ind], nums[i] = nums[i], nums[ind]
                break

        nums[ind + 1:] = reversed(nums[ind + 1:])

solution = Solution()
nums = [1, 2, 3]
solution.nextPermutation(nums)
print(nums)
        
