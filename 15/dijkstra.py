from icecream import ic
import cProfile
import heapq
nodes = []
edges = {}
data = []

class Node:
    def __init__(self, _id, weight):
        self.uid = _id
        self.weight = weight if weight < 10 else weight%9
        self.visited =False
        self.distance =9999999
    def hash(self):
        return self.uid
    def __repr__(self):
        return f"{self.weight}"


with open("input.txt", 'r') as fin:
    fin = fin.readlines()
    '''
    fin = [ 
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581",
        ]
    '''
    _id = 0
    for i in range(5):
        for line in fin:
            for j in range(5):
                line=line.strip()
                if i==0 and j==0: data.append(line)
                for a in line:
                    nodes.append(Node(_id, int(a)+i+j))
                    _id+=1

for i in range(50):
    print("".join([str(x.weight) for x in nodes[50*i:50+50*i]]))

for i in range(len(data)*5):
    for j in range(len(data[0])*5):
        node_i = i*len(data)*5+j
        if i == 0:
            if j==0:
                edges[node_i] = [nodes[node_i+1], nodes[node_i+len(data[0])*5]]
            elif j==len(data)*5-1:
                edges[node_i] = [nodes[node_i-1], nodes[node_i+len(data[0])*5]]
            else:
                edges[node_i] = [nodes[node_i+1], nodes[node_i-1], nodes[node_i+len(data[0])*5]]
        elif i == len(data)*5-1:
            if j==0:
                edges[node_i] = [nodes[node_i+1], nodes[node_i-len(data[0])*5]]
            elif j==len(data)*5-1:
                edges[node_i] = [nodes[node_i-1], nodes[node_i-len(data[0])*5]]
            else:
                edges[node_i] = [nodes[node_i+1], nodes[node_i-1], nodes[node_i-len(data[0])*5]]
        else:
            if j==0:
                edges[node_i] = [nodes[node_i+1], nodes[node_i+len(data[0])*5], nodes[node_i-len(data[0])*5]]
            elif j==len(data)*5-1:
                edges[node_i] = [nodes[node_i-1], nodes[node_i+len(data[0])*5], nodes[node_i-len(data[0])*5]]
            else:
                edges[node_i] = [nodes[node_i+1], nodes[node_i-1], nodes[node_i-len(data[0])*5], nodes[node_i+len(data[0])*5]]


distance = []
prev = []
todo = []
visited = set()
for node in nodes:
    if node.uid != 0:
        heapq.heappush(distance, (9999999,node.uid))
    prev.append(None)
    todo.append(node)

heapq.heappush(distance, (0,0))

def dijk(todo, distance, prev, visited):
    while len(todo):
        if len(todo)%1000 == 0:
            ic(len(todo))
        next_node = heapq.heappop(distance)
        curr_path = next_node[0]
        next_node_i = todo.index(nodes[next_node[1]])
        next_node = todo.pop(next_node_i)
        next_node.visited=True
        for node in edges[next_node.uid]:
            if node.weight+curr_path < nodes[node.uid].distance and not node.visited:
                heapq.heappush(distance, (node.weight + curr_path, node.uid))
                node.distance = node.weight+curr_path
                prev[node.uid] = next_node.uid

dijk(todo, distance, prev, visited)
#cProfile.run('dijk(todo, distance, prev, visited)')

#Now sum the path
def find_path(start_id):
    path = []
    while start_id!=0:
        path.append(start_id)
        start_id=prev[start_id]
    return reversed(path)

path = find_path(len(nodes)-1)
ic(path)

score = sum([nodes[x].weight for x in path])
ic(score)
