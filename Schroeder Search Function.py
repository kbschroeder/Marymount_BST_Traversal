class new_node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, value):
    # Traverse untill root reaches
    # to dead end
    while root != None:

        # pass right subtree as new tree
        if value > root.data:
            root = root.right

            # pass left subtree as new tree
        elif value < root.data:
            root = root.left
        else:
            return True  # if the key is found return 1
    return False


def insert(Node, data):
    # If the tree is empty, return
    # a new Node
    if Node == None:
        return new_node(data)

    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)

    return Node

if __name__ == '__main__':

    root = None
    root = insert(root, 5)
    insert(root, 3)
    insert(root, 2)
    insert(root, 4)
    insert(root, 7)
    insert(root, 6)
    insert(root, 8)
    if search(root, 1):
        print("Yes")
    else:
        print("No")