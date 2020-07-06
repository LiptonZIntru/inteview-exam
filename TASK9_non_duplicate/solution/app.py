# Task 9 finished at 6.7.2020 13:37
def singleNumber(nums):
    nums.sort()
    for i in range(round(len(nums) / 2)):
        if not nums[2 * i] == nums[2 * i + 1]:
            return nums[2 * i]
    return "Everything is ok"


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
