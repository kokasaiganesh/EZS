class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


if __name__ == "__main__":
    root = None

    
    root = insert(root, 100)
    root = insert(root, 70)
    root = insert(root, 50)
    root = insert(root, 60)
    root = insert(root, 9)
    root = insert(root, -3)
    print('inorder traversal of given tree')
    inorder(root)

    
    search_key = int(input('enter value to search in bst'))
    result = search(root, search_key)
    if result is not None:
        print(f" {search_key} found in the BST.")
    else:
        print(f" {search_key} not found in the BST.")

    
    
