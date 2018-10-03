import base64
from random import randint

string = "https://docs.python.org/2/library/base64.html"


def hashAn(s, digits):
    slice1 = randint(5, 10)
    slice2 = randint(11, 16)
    key = s[slice1:slice2]

    hs = base64.b64encode(key.encode()) + base64.b32encode(len(string) % 256)
    return hs


print(hashAn(string, 2))
