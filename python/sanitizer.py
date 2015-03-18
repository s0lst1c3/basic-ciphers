from string import lowercase
from string import uppercase

def sanitize(dirty):

    clean = []
    dirty = list(dirty)

    for d in dirty:
        if d in lowercase:
            clean.append(d)
        if d in uppercase:
            clean.append(chr(ord(d)+32))
    return ''.join(clean)
