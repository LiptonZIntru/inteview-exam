# Task 7 finished at 4.7.2020 22:35
import time
import random
def sortNums(nums):
    # Fill this in.
    arr = {
        0: [],
        1: [],
        2: []
    }
    arr[0].append(nums[0])
    for i in nums[1:len(nums)]:
        if arr[0][0] == i:
            arr[0].append(i)
        else:
            if not arr[1]:
                arr[1].append(i)
            elif arr[1][0] == i:
                arr[1].append(i)
            else:
                arr[2].append(i)
    for i in range(len(arr) - 1):
        for a in range(len(arr) - 1):
            if arr[i][0] > arr[a + 1][0]:
                pom = arr[i]
                arr[i] = arr[a + 1]
                arr[a + 1] = pom
    return arr[0] + arr[1] + arr[2]
    '''
    for i in nums[0:len(nums) - 1]:
        for a in nums[1:len(nums)]:
            if i > a:
                pom = i
                i = a
                a = pom
    return nums'''


arr = []
for i in range(10000):
    arr.append(random.randint(1, 3))
b = time.time()
# print(sortNums([3, 3, 2, 1, 3, 2, 1]))
print(sortNums(arr))
print(time.time() - b)
# [1, 1, 2, 2, 3, 3, 3]
