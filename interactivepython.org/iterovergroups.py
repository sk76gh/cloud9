from itertools import groupby
tlist = [('a',1), ('a',2), ('a',3), ('b',1), ('b',2), ('c',1), ('c',2), ('c',3), ('d',1) ]

groups = groupby(tlist, key=lambda x: x[0])

for key, group in groups:
    print key,group
    print(key)
    for thing in group:
        print(thing)