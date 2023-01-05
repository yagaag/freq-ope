from .key import cointoss
from .aes import AESCipher
from .server import OPEServer

class OPEClient(object):

    def __init__(self, aes: AESCipher, ope: OPEServer):
        self.aes = aes
        self.ope = ope
    
    def add_plaintext(self, val: int):
        
        s = ''
        match = "g"
        add_val = self.ope.M//2
        
        start = 0
        end = self.ope.M
        ct = 0

        while True:
            ct+=1
            if ct == self.ope.M:
                return False
            mid = (end+start) // 2
            v = self.ope.val_at_tree_pos(self.ope.root, s)
            if not v:
                add_val = mid
                if match != 'm' and s and cointoss():
                    s = s[:-1]
                    node = self.ope.get_node(self.ope.root, s)
                    self.ope.root = self.ope.add(self.ope.root, s, add_val)
                    if match == 'l':
                       self.ope.root = self.ope.add_node(self.ope.root, s+'1', node)
                    else:
                        self.ope.root = self.ope.add_node(self.ope.root, s+'0', node)
                else:
                    self.ope.root = self.ope.add(self.ope.root, s, add_val)
                self.ope.add_to_dct(add_val, self.aes.encrypt(str(val)))
                return True
            cipher = self.ope.dct[v]
            tree_val = self.aes.decrypt(cipher)
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