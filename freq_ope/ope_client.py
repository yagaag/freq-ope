from .key import cointoss
from .aes_cipher import AESCipher
from .ope_server import OPE_Server

class OPE_Client(object):

    def __init__(self, aes: AESCipher, ope: OPE_Server):
        self.aes = aes
        self.ope = ope
    
    def add_plaintext(self, val):
        
        s = ''
        done = False
        match = "g"
        what_to_add = self.ope.M//2
        
        start = 0
        end = self.ope.M

        while not done:
            mid = (end+start) // 2
            v = self.ope.val_at_tree_pos(self.ope.root, s)
            if not v:
                what_to_add = mid
                if match != 'm' and s and cointoss():
                    s = s[:-1]
                    node = self.ope.get_node(self.ope.root, s)
                    ct = self.ope.dct[node.val]
                    self.ope.root = self.ope.add(self.ope.root, s, what_to_add)
                    if match == 'l':
                       self.ope.root = self.ope.add_node(self.ope.root, s+'1', node)
                    else:
                        self.ope.root = self.ope.add_node(self.ope.root, s+'0', node)
                else:
                    self.ope.root = self.ope.add(self.ope.root, s, what_to_add)
                self.ope.add_to_dct(what_to_add, self.aes.encrypt(str(val)))
                return
            cipher = self.ope.dct[v]
            tree_val = self.aes.decrypt(cipher)
            prev_val = v
            if val < int(tree_val):
                match = "l"
                s += '0'
                end = v
            elif val > int(tree_val):
                match = "g"
                s += '1'
                start = v
            else:
                match = "m"
                if cointoss():
                    s += '1'
                    start = v
                else:
                    s += '0'
                    end = v