mem = {
        0:1,
        1:1,
        2:1,
        3:1,
        4:1,
        5:1,
        6:1,
        }
#mem[x] = mem[x-7] + mem[x-9]
for i in range(7,800):
    mem[i] = mem.get(i-7, 0) +mem.get(i-9, 0)
from pprint import pprint
pprint(mem)
