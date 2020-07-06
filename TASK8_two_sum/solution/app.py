# Task 7 finished at 4.7.2020 23:40
import time
import random
def two_sum(list, k):
    list.sort()
    head1 = 0
    head2 = len(list) - 1
    for i in range(len(list)):
        if list[head1] + list[head2] == k:
            print(list[head1], list[head2], k)
            return True
        elif list[head1] + list[head2] > k:
            head2 -= 1
        elif list[head1] + list[head2] < k:
            head1 += 1
        if head1 > head2:
            return False

def two_sum_check(list, k):
    for a in list:
        for b in list:
            if a + b == k:
                print(a, b, k)
                return True
    return False


arr_answers = []
for b in range(100):
    arr = []
    for i in range(100):
        arr.append(random.randint(1, 100))
    k = random.randint(99, 10000)
    arr_answers.append(two_sum_check(arr, k) == two_sum(arr, k))
print(arr_answers)
print(arr_answers.__contains__(False))
a = time.time()
# print(two_sum([4,7,1,-3,2], 5))
# print(two_sum(arr, 40))
# print(time.time() - a)
# True