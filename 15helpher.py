import networkx as nx
import time


def do(kek, l):
    kek = [int(k) for k in kek]

    s = 0
    for i in range(len(kek)):
        if i % l != l - 1:
            print("%i\n%i\n%i" % (i, i + 1, kek[i]))
            s += 1
        if i % l != 0:
            print("%i\n%i\n%i" % (i, i - 1, kek[i]))
            s += 1
        if i // l != 0:
            print("%i\n%i\n%i" % (i, i - l, kek[i]))
            s += 1
        if i // l != l - 1:
            print("%i\n%i\n%i\n" % (i, i + l, kek[i]))
            s += 1
    print(s)

from input_fuenfzehn import kek

do(kek, 100)
