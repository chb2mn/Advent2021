
my_map = []
with open('input.txt', 'r') as fin:
#with open('test.txt', 'r') as fin:
    for line in fin:
        my_map.append([int(x) for x in line.strip()])

safe_spots = []
safe_coordinates = []
for y, row in enumerate(my_map):
    for x, val in enumerate(row):
        if y>0 and val >= my_map[y-1][x]:
            continue
        if y < len(my_map)-1 and val >= my_map[y+1][x]:
            continue
        if x > 0 and val >= my_map[y][x-1]:
            continue
        if x < len(row)-1 and val >= my_map[y][x+1]:
            continue
        safe_spots.append(val)
        safe_coordinates.append((x,y))

'''
part 1
print(safe_spots)
print(sum(safe_spots) + len(safe_spots))
'''

'''
part 2
'''
def build_basin(my_map, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    #print("Checking: ",x,y)
    basin = {(x,y)}
    val = my_map[y][x]
    if val == 9:
        return {}
    #print("Adding: ",x,y)
    if y-1>=0 and val < my_map[y-1][x]:
        basin = basin.union(build_basin(my_map, (x,y-1)))
    if y+1 < len(my_map) and val < my_map[y+1][x]:
        basin = basin.union(build_basin(my_map, (x,y+1)))
    if x-1 >= 0 and val < my_map[y][x-1]:
        basin = basin.union(build_basin(my_map, (x-1,y)))
    if x+1 < len(my_map[y]) and val < my_map[y][x+1]:
        basin = basin.union(build_basin(my_map, (x+1,y)))
    return basin

max_3 = []
spot2basin = {}
for i, spot in enumerate(safe_coordinates):
    #print("new spot:", spot)
    basin = build_basin(my_map, spot)
    spot2basin[spot] = basin
    max_3.append(len(basin))
    max_3.sort()
    if len(max_3) > 3: 
        max_3.pop(0)

print(max_3)
print(max_3[0]*max_3[1] * max_3[2])

'''
from pprint import pprint
pprint(spot2basin)
''' 


