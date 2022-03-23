# Checking if a binary tree is height balanced in Python
#code taken from https://www.programiz.com/dsa/balanced-binary-tree

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isHeightBalanced(root, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)
    print("r:",r)
    print("l",l)
    height.height = max(left_height.height, right_height.height) + 1
    print("height:",height.height)
    print("root:",root.data)

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if isHeightBalanced(root, height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')
