# Author: s0lst1c3
# Description: Simple implementation of the vigenere ciphere

import random
from sanitizer import sanitize
from string import lowercase

random.seed()

OFFSET = ord('a')

def gen(keysize):
    return ''.join(random.sample(lowercase, keysize))

def enc(m, k):
    m = sanitize(m)
    c = []
    k_len = len(k)

    for i in xrange(0, len(m)):
        c.append(chr((ord(m[i])-OFFSET+ord(k[i%k_len])-OFFSET)%26+OFFSET))

    return ''.join(c)

def dec(c, k):
    m = [] 
    k_len = len(k)

    for i in xrange(0, len(c)):
        m.append(chr(((ord(c[i])-OFFSET)-(ord(k[i%k_len])-OFFSET))%26+OFFSET))

    return ''.join(m)

