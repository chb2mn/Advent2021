from copy import deepcopy
from icecream import ic

data = [
        "qi-UD",
        "jt-br",
        "wb-TF",
        "VO-aa",
        "UD-aa",
        "br-end",
        "end-HA",
        "qi-br",
        "br-HA",
        "UD-start",
        "TF-qi",
        "br-hf",
        "VO-hf",
        "start-qi",
        "end-aa",
        "hf-HA",
        "hf-UD",
        "aa-hf",
        "TF-hf",
        "VO-start",
        "wb-aa",
        "UD-wb",
        "KX-wb",
        "qi-VO",
        "br-TF",
        ]
'''
data = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
        ]

data = [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW",
]
'''


my_map = {}

for line in data:
    parts = line.strip().split("-")
    try:
        my_map[parts[0]].add(parts[1])
    except KeyError:
        my_map[parts[0]] = {parts[1]}
    try:
        my_map[parts[1]].add(parts[0])
    except KeyError:
        my_map[parts[1]] = {parts[0]}

ic(my_map)

def cave_conditional(path, next_node):
    #part 2 logic
    my_bool=True
    if not next_node.islower():
        return my_bool
    if next_node =='start':
        my_bool=False
        return my_bool
    allowance=1
    for i in set(path):
        if i.islower() and path.count(i) ==2:
            if allowance:
                allowance -=1
            else:
                my_bool = False
                return my_bool
        if i.islower() and path.count(i) > 2:
            my_bool = False
            return my_bool
    
    return my_bool

def find_paths(my_map, node, path=[]):
    path += [node]
    if node == 'end':
        return path
    paths = []
    for next_node in my_map[node]:
        if cave_conditional(path, next_node):
            appended_path = find_paths(my_map, next_node, deepcopy(path))
            if len(appended_path) and isinstance(appended_path[0], list): 
                paths.extend(appended_path)
            else:
                paths.append(appended_path)
    return paths

def prune_paths(paths):
    return [x for x in paths if len(x) and x[-1] == 'end']

all_paths = find_paths(my_map, 'start')
pruned_paths = prune_paths(all_paths)
ic(pruned_paths)
print(len(pruned_paths))
