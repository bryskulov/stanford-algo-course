class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class BST:
    def __init__(self):
        self.root = BSTNode()
    
    def no_child(self, node):
        '''Return True if the node does not have any children nodes'''
        if node.left == None and node.right == None:
            return True
        else:
            return False

    def search(self, key, node=None):
        '''
        Searches for the key in the tree and returns the node with that key.
        If the key does not exist returns the closest node
        '''
        if node == None:
            node = self.root
        if node.val == key or self.no_child(node) == True:
            return node
        elif node.val > key:
            if node.left == None:
                return node
            return self.search(key, node.left)
        else:
            if node.right == None:
                return node
            return self.search(key, node.right)

    def insert(self, key, root=False):
        '''
        Inserts the key into the tree
        '''
        if root == True:
            print('Inserted root value: ', key)
            self.root.val = key
            pass
        node = self.search(key)
        if node.val > key:
            print('Inserted to left: ', key)
            node.left = BSTNode(val=key)
        elif node.val < key:
            print('Inserted to right: ', key)
            node.right = BSTNode(val=key)
        else:
            pass
    
    def get_max(self):
        current_node = self.root
        while current_node.right != None:
            current_node = current_node.right
        return current_node
    
    def get_min(self):
        current_node = self.root
        while current_node.left != None:
            current_node = current_node.left
        return current_node

    def inorder(self, node='root'):
        '''
        Traverse the tree in order and print the keys
        '''
        if node == 'root':
            node = self.root
        if node is not None:
            self.inorder(node.left)
            print(str(node.val) + "->", end=' ')
            self.inorder(node.right)

# Note: Predecessor, successor and delete methods are to be implemented.
#       The difficulty is to efficiently recurse the tree up to its parents.
        
def main():
    bst = BST()
    bst.insert(3, root=True)
    bst.insert(1)
    bst.insert(2)
    bst.insert(5)
    bst.insert(4)
    print(bst.search(0).val)
    print(bst.search(2).val)
    print(bst.get_max().val)
    print(bst.get_min().val)
    bst.inorder()


if __name__ == '__main__':
    main()