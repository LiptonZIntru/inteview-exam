# Task 1: finished v 1:18 26.6.2020


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        result = ListNode(l1.val + l2.val + c)
        c = 0
        if l1.val + l2.val >= 10:
            c = 1

        if l1.next and l2.next:
            num = self.addTwoNumbers(l1.next, l2.next, c=c)
            if num.val >= 10:
                num.val = num.val - 10
            result.next = num
        return result
    # Fill this in.

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 8
