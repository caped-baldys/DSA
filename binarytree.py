

class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root == None:
        return
    print(root.data,end=':')
    if root.left is not None:
        print('L ',root.left.data,end="  ")
    if root.right is not None:    
        print("R ",root.right.data,end="  ")
    print()
    printTree(root.left)
    printTree(root.right)

def countNodes(root):
    if root == None:
        return 0
    leftcount = countNodes(root.left)
    rightcount = countNodes(root.right)
    return (leftcount + rightcount + 1)


def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root
root = treeInput()
printTree(root)
print(countNodes(root))

# bt1 = BinaryTreeNode(1)
# bt2 = BinaryTreeNode(2)
# bt3 = BinaryTreeNode(3)


# bt1.left = bt2
# bt1.right = bt3

# printTree(bt1)