# Basic Node definition. Each Node contains a Value, a left child, and a right child
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


# insert Value into the appropriate spot in the tree
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder_traversal(root):
    # finish code to print all values with an inorder traversal
    if root:
        inorder_traversal(root.left)
        print(root.val),
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)

        print(root.val),

def preorder_traversal(root):
    if root:
        print(root.val),
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def search(root, value):

    #Base Cases: root is cull
    if root is None or root.val == value:
        return root

    #Value is greater than root's value
    if root.val < value:
        return search(root.right, value)

    # Value is smaller than root's value
    return search(root.left,value)


bst_root = Node(5)
insert(bst_root,Node(2))
insert(bst_root,Node(7))
insert(bst_root,Node(10))
insert(bst_root,Node(4))
insert(bst_root,Node(1))

print("\nPreorder traversal is: ")
preorder_traversal(bst_root)

print("\ninorder traversal is: ")
inorder_traversal(bst_root)

print("\nPostorder traversal is: ")
postorder_traversal(bst_root)




