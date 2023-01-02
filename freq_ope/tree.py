class TreeNode():
    
    def __init__(self, e=0, left=None, right=None):
        self.val = e
        self.left = left
        self.right = right
    
    # Inorder traversal of tree
    def inorderTraversal(self):
        
        # Using recursion: O(n) time; O(n) space
        def inorder(node, ls): 
            if node:
                inorder(node.left, ls)
                ls.append(node.val)
                inorder(node.right, ls)
        ls = []
        inorder(self, ls)
        return ls