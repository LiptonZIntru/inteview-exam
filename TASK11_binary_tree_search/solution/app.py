# Task finished at 6.7.2020 17:31
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    result = [floor, ceil]
    if floor is None:
        if k - root_node.value > 0:
            result[0] = root_node.value
    if ceil is None:
        if k - root_node.value < 0:
            result[1] = root_node.value

    if root_node.left:
        result = findCeilingFloor(root_node.left, k, floor=result[0], ceil=result[1])
    if root_node.right:
        result = findCeilingFloor(root_node.right, k, floor=result[0], ceil=result[1])

    if 0 < k - root_node.value < k - result[0]:
        result[0] = root_node.value
    if 0 > k - root_node.value > k - result[1]:
        result[1] = root_node.value
    return result


# Fill this in.

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
