from icecream import ic
import math
from copy import deepcopy

global_beacons = []

class Scanner:
    def __init__(self):
        self.beacons = []
        self.x=None
        self.y=None
        self.z=None
        self.distances = None

    def add_beacon(self, x,y,z):
        self.beacons.append([int(x),int(y),int(z)])

    def get_distances(self):
        if self.distances is None:
            self.distances = []
            for i,b in enumerate(self.beacons):
                self.distances.append([])
                for b2 in self.beacons:
                    self.distances[i].append(calc_dist(b,b2))
        return self.distances

    def rotate(self, axis):
        if axis ==0:
            '''backspin'''
            for b in self.beacons:
                temp = b[1]
                b[1] = -b[2]
                b[2]=temp
        elif axis==1:
            '''corkscrew right'''
            for b in self.beacons:
                temp = b[0]
                b[0]=b[2]
                b[2]=-temp
        elif axis==2:
            '''frisbee right-hand backhand'''
            for b in self.beacons:
                temp = b[0]
                b[0] = b[1]
                b[1] =-temp

    def translate(self, x,y,z):
        self.beacons = [[a[0]+x,a[1]+y,a[2]+z] for a in self.beacons]
    def untranslate(self, x,y,z):
        self.beacons = [[a[0]-x,a[1]-y,a[2]-z] for a in self.beacons]

def calc_dist(beacon1, beacon2):
    if len(beacon1) > 2:
        return math.sqrt(((beacon1[0]-beacon2[0])**2)+
                ((beacon1[1]-beacon2[1])**2)+
                ((beacon1[2]-beacon2[2])**2)
                    )
    else:
        return math.sqrt(((beacon1[0]-beacon2[0])**2)+((beacon1[1]-beacon2[1])**2))

def num_matches(l1, l2):
    l1 = sorted(l1)
    l2 = sorted(l2)
    num_matches = 0
    for dist in l1:
        if dist in l2:
            num_matches+=1
    return num_matches

def close_enough(scan1, scan2):
    scan1_dist = scan1.get_distances()
    scan2_dist = scan2.get_distances()
    identical_beacons = []
    for i, distances_1 in enumerate(scan1_dist):
        for j, distances_2 in enumerate(scan2_dist):
            if num_matches(distances_1,distances_2) >= 12:
                identical_beacons.append((i,j))
    return identical_beacons

def align_scanners(scan1, scan2, identical_beacons):
    ic(identical_beacons)
    my_scan2 = deepcopy(scan2)
    found_beacons1 = [scan1.beacons[x[0]] for x in identical_beacons]
    found_beacons2 = [scan2.beacons[x[1]] for x in identical_beacons]
    x = 0
    y = 0
    z = 0
    translate_vector = [
            found_beacons1[0][0] - found_beacons2[0][0],
            found_beacons1[0][1] - found_beacons2[0][1],
            found_beacons1[0][2] - found_beacons2[0][2],
            ]
    my_scan2.translate(*translate_vector)
    found_beacons2 = [my_scan2.beacons[x[1]] for x in identical_beacons]
    
    while found_beacons1[1] != found_beacons2[1]:
        my_scan2.untranslate(*translate_vector)
        if x < 4:
            my_scan2.rotate(0)
            scan2.rotate(0)
            x+=1
        elif y < 4:
            my_scan2.rotate(1)
            scan2.rotate(1)
            y+=1
            x=0
        elif z < 4:
            my_scan2.rotate(2)
            scan2.rotate(2)
            x=0
            y=0
            z+=1
        else:
            print("UHHH")
            print(x,y,z)
            quit()
        found_beacons2 = [my_scan2.beacons[x[1]] for x in identical_beacons]
        translate_vector = [
                found_beacons1[0][0] - found_beacons2[0][0],
                found_beacons1[0][1] - found_beacons2[0][1],
                found_beacons1[0][2] - found_beacons2[0][2],
                ]
        my_scan2.translate(*translate_vector)
        found_beacons2 = [my_scan2.beacons[x[1]] for x in identical_beacons]
    ic(translate_vector)
    return my_scan2, translate_vector

scanners = []

with open('input.txt', 'r') as fin:
    for line in fin:
        if line.strip() =='':
            continue
        elif line.startswith('--'):
            scanners.append(Scanner())
        else:
            scanners[-1].add_beacon(*line.split(','))
num_beacons = 0
global_beacons = set([tuple(x) for x in scanners[0].beacons])
global_scanner_pos = [[0,0,0]]
todo = [0]
done = []
while len(todo):
    i = todo.pop(0)
    for j in range(len(scanners)):
        if i !=j:
            close = close_enough(scanners[i], scanners[j])
            if len(close):
                ic(i)
                ic(j)
                aligned_scanner, tv = align_scanners(scanners[i],scanners[j], close)
                global_scanner_pos.append(tv)
                scanners[j] = aligned_scanner
                global_beacons = global_beacons.union(set(tuple(x) for x in scanners[j].beacons))
                if j not in done:
                    todo.append(j)
                    done.append(j)

ic(global_beacons)
ic(len(global_beacons))
def manhattan_distance(v1, v2):
    return (v1[0]-v2[0]) + (v1[1]-v2[1]) + (v1[2]-v2[2])

max_manhattan = 0
for i in global_scanner_pos:
    for j in global_scanner_pos:
        max_manhattan=max(max_manhattan, manhattan_distance(i,j))
ic(max_manhattan)
