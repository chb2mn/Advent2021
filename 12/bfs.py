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
my_map = {}
for line in data:
    parts = line.strip().split('-')
    try:
        my_map[parts[0]].add(parts[1])
    except KeyError:
        my_map[parts[0]] = {parts[1]}
    try:
        my_map[parts[1]].add(parts[0])
    except KeyError:
        my_map[parts[1]] = {parts[0]}

ic(my_map)

paths = []

def bfs(my_map):
