#grab assesment practice
#code taken from https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/

class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def maxSumBetweenLeaves_aux(current,res):
    print("."*20)

    if current is None:
        return 0
    print("current:", current.data)

    left=maxSumBetweenLeaves_aux(current.left,res)
    right=maxSumBetweenLeaves_aux(current.right,res)
    if current.right is not None and current.left is not None:
        res[0]=max(res[0],left+right+current.data)
        print("current",current.data)
        print("left:", left,"right:",right)
        return max(left,right) + current.data

    if current.left is None:
        print("second if statement")
        print(right+current.data)
        return right+current.data
    else:
        print("second if statement")
        print(right + current.data)
        return left +current.data


def maxSumBetweenLeaves(root):
    res=[0]
    maxSumBetweenLeaves_aux(root,res)
    print(res[0])

if __name__ == '__main__':
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)
    maxSumBetweenLeaves(root)