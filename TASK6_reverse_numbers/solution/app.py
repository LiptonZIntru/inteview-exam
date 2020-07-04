# Task 6 finished at 19:19 4.7.2020
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution
    def reverseIteratively(self, head):
        '''
        FIRST SOLUTION:
        nodes = []
        i = 0
        while head:
            nodes.append(ListNode(head.val))
            if not i == 0:
                nodes[i].next = nodes[i - 1]
            head = head.next
            i = i + 1
        return nodes[len(nodes) - 1]
        '''
        result = ListNode(head.val)
        while head.next:
            node = ListNode(head.next.val)
            node.next = result
            result = node
            head = head.next
        return result

    # Recursive Solution
    def reverseRecursively(self, head):
        result = ListNode(head.val)
        if head.next:
            result = self.reverseRecursively(head.next)
            node = result
            while node.next:
                node = node.next
            node.next = ListNode(head.val)
        return result


# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testTail = testHead.reverseIteratively(testHead)
# testTail = testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
