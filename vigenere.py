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
        char = m[i]
        char = ord(char)
        char -= OFFSET
        char = (char + ord(k[i % k_len])) % 26
        char += OFFSET
        char = chr(char)
        c.append(char)

    return ''.join(c)

def dec(c, k):
   
    m = [] 
    k_len = len(k)
    for i in xrange(0, len(c)):
        char = c[i]
        char = ord(char)
        char -= OFFSET
        char = (char - ord(k[i % k_len])) % 26
        char += OFFSET
        char = chr(char)
        m.append(char)

    return ''.join(m)












