class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"


def swap_every_two(llist):
    if llist is None or llist.next is None:
        return llist
    third = llist.next.next
    new = llist.next
    new.next = llist
    new.next.next = swap_every_two(third)
    return new


llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(swap_every_two(llist))
# 2, (1, (4, (3, (5, (None)))))