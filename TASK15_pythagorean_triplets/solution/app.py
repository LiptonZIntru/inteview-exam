# Task 15 finished at 8.7.2020 1:19
def findPythagoreanTriplets(nums):
    nums.sort()
    while len(nums) > 2:
        target = nums.pop()
        for b in nums:
            for c in nums[nums.index(b) + 1: len(nums)]:
                if b ** 2 + c ** 2 == target ** 2:
                    return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
