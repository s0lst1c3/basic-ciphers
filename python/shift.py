# Author: s0lst1c3
# Description: Simple shift cipher implemented in Python.

from random import randint, seed
from sanitizer import sanitize

seed()

OFFSET = ord('a')

def gen():
    return randint(0, 25)

def enc(m, k):
    m = sanitize(m)
    
    c = []
    for char in m:
        c.append(chr((((ord(char)-OFFSET)+k)%26)+OFFSET))
    return ''.join(c)

def dec(c, k):
    
    m = []
    for char in c:
        m.append(chr((((ord(char)-OFFSET)-k)%26)+OFFSET))
    return ''.join(m)
