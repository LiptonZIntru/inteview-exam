# Task 10 finished at 6.7.2020 14:22
def check(lst):
    popped = False

    for i in range(len(lst) - 1):
        if popped and i == len(lst) - 1:
            break
        if not lst[i] < lst[i + 1]:
            if not popped:
                lst.pop(i)
                popped = True
                i -= 1
            else:
                return False
    return True


print(check([13, 4, 7]))
# True
print(check([5, 1, 3, 2, 5]))
# False
