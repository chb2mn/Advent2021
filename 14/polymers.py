from icecream import ic
from copy import deepcopy
import cProfile
from collections import Counter
from functools import lru_cache

expansion = {}
mer = ""
with open('input.txt', 'r') as fin:
    '''
    fin = [
            "NNCB",
            "",
            "CH -> B",
            "HH -> N",
            "CB -> H",
            "NH -> C",
            "HB -> C",
            "HC -> B",
            "HN -> C",
            "NN -> C",
            "BH -> H",
            "NC -> B",
            "NB -> B",
            "BN -> B",
            "BB -> N",
            "BC -> B",
            "CC -> N",
            "CN -> C",
            ]
    '''
    phase = 0
    for line in fin:
        line=line.strip()
        if line == "":
            phase += 1
        elif phase:
            ic(line)
            paths = line.split(" -> ")
            expansion[paths[0]] = f"{paths[1]}"
        else:
            mer = line.strip()

ic(expansion)
ic(mer)

@lru_cache(maxsize=None)
def expand_mer(mer, n):
    if n == 0:
        return Counter(mer)
    elif len(mer) >2:
        #remove the duplicates
        return sum([expand_mer(mer[i:i+2], n) for i in range(len(mer)-1)], Counter()) - Counter(mer[1:-1]) 
    new_letter = expansion[mer]
    return expand_mer(mer[0]+new_letter, n-1) + expand_mer(new_letter+mer[1], n-1) - Counter(new_letter)

mer = expand_mer(mer, 40)
ic(mer)
ic(mer.most_common()[0][1] - mer.most_common()[-1][1])
