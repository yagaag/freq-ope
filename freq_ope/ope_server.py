from .tree import TreeNode

class OPE_Server(object):

    root, size = None, 0

    def __init__(self, M):
        self.M = M
        self.length = 0
        self.root = None
        self.dct = {}
    
    def val_at_tree_pos(self, node, s):
        if s == '':
            return node.val if node else None
        if len(s) != 1:
            if s[0] == '0':
                return self.val_at_tree_pos(node.left, s[1:]) if node.left else None
            else:
                return self.val_at_tree_pos(node.right, s[1:]) if node.right else None
        else:
            if s[0] == '0':
                return node.left.val if node.left else None
            else:
                return node.right.val if node.right else None
        
    def add(self, node, s, val):
        if not s or node is None:
            node = TreeNode(val)
        else:
            if len(s) == 1:
                if s[0] == '0':
                    node.left = TreeNode(val)
                else:
                    node.right = TreeNode(val)
            else:
                if s[0] == '0':
                    node.left = self.add(node.left, s[1:], val)
                else:
                    node.right = self.add(node.right, s[1:], val)
        self.length += 1
        return node
    
    def add_node(self, node, s, n):
        if not s or node is None:
            node = n
        else:
            if len(s) == 1:
                if s[0] == '0':
                    node.left = n
                else:
                    node.right = n
            else:
                if s[0] == '0':
                    node.left = self.add_node(node.left, s[1:], n)
                else:
                    node.right = self.add_node(node.right, s[1:], n)
        self.length += 1
        return node
        
    def get_node(self, node, s):
        if s == '':
            return node if node else None
        if len(s) != 1:
            if s[0] == '0':
                return self.get_node(node.left, s[1:]) if node.left else None
            else:
                return self.get_node(node.right, s[1:]) if node.right else None
        else:
            if s[0] == '0':
                return node.left if node.left else None
            else:
                return node.right if node.right else None
        
    def add_to_dct(self, key, val):
        self.dct[key] = val