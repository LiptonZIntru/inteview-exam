class Solution:
    def moveZeros(self, nums):
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]