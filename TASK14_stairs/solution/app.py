# Task finished at 6.7.2020 22:57
def staircase(n):
    # Fill this in.
    val1 = 1
    val2 = 1
    for i in range(n - 1):
        val1 += val2

        help_var = val1
        val1 = val2
        val2 = help_var
    return val2


print(staircase(4))
# 5
print(staircase(5))
# 8
