import random

def keygen(bits):
    key = 0
    for i in range(bits-1):
        if random.randrange(0,1e10) % 2:
            key += (2**i)
    key+= (2**(bits-1))
    return bin(key)

def cointoss():
    r = random.randrange(0,1e10)
    if r % 2:
        return 1
    return 0