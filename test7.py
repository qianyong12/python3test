from typing import List, Set, Dict, Deque
from pythonds.basic import queue, stack, deque
# from collections import deque

def func():
    l = input()
    m = []
    while (l != ''):
        m.append(list(l.strip().split(',')))
        l = input()
    m = sorted(m, key=lambda x: (int(x[2])), reverse=True)
    print(m)


if __name__ == "__main__":
    # l=list(set(['a','b','c']))
    l = list({'a', 'b', 'c'})  # set={} list=[] tunal=() dict={key=value,...}
    q = deque
    # l=set(['a','b','c'])
    print(l[0])
    func()
