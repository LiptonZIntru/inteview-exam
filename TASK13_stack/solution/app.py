# Task 13 finished at 6.7.2020 20:38
class MaxStack:
    def __init__(self):
        self.values = []
        self.max_val = None

    def push(self, val):
        self.values.append(val)
        if self.max_val is None:
            self.max_val = val
        if self.max_val < val:
            self.max_val = val

    def pop(self):
        value = self.values.pop()
        if value == self.max_val:
            self.max_val = max(self.values)

    def max(self):
        return self.max_val


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
