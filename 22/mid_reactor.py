from icecream import ic
from copy import deepcopy

def intersects(cube1, cube2): #[10..12][11..13], [10..13][11..12], [11..13][10..12], [11..12][10..13]
    for i in range(3):
        if not(cube1[i][0] <= cube2[i][1] and cube2[i][0] <= cube1[i][1]):
            return False
    return True

def total_intersects(cube1, cube2): #[1,3][1,3][1,3] [2,2][2,2][2,2]
    c1axis = []
    c2axis = []
    for i in range(3):
        c1axis.append(cube1[i][0] <= cube2[i][0] and cube1[i][1]>=cube2[i][1])
                
    #for i in range(3):
    #    c2axis.append(cube1[i][0] >= cube2[i][0] and cube1[i][1]<=cube2[i][1])
    return all(c1axis)# or all(c2axis)

def split(cube1, cube2):
    '''always split cube 2'''
    '''x-axis'''
    ic(cube1)
    ic(cube2)
    if cube2[0][0] <= cube1[0][1] and cube2[0][1] >= cube1[0][1]:
        if cube2[0][1] == cube[0][1]:
            return cube1, [[cube2[0][0],cube1[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]], [[cube1[0][1],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]]
        return cube1, [[cube2[0][0],cube1[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]], [[cube1[0][1]+1,cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]]
    elif cube2[0][0] <= cube1[0][0] and cube2[0][1] >= cube1[0][0]:
        if cube2[0][1] == cube[0][1]:
            return cube1,[[cube2[0][0],cube1[0][0]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]], [[cube1[0][0],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]]
        return cube1,[[cube2[0][0],cube1[0][0]-1],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]], [[cube1[0][0],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube2[2][1]]]
    #y-axis
    elif cube2[1][0] <= cube1[1][1] and cube2[1][1] >= cube1[1][1]:
        return cube1,  [[cube2[0][0],cube2[0][1]],[cube2[1][0],cube1[1][1]],[cube2[2][0],cube2[2][1]]], [[cube2[0][0],cube2[0][1]],[cube1[1][1]+1,cube2[1][1]]  ,[cube2[2][0],cube2[2][1]]]
    elif cube2[1][0] <= cube1[1][0] and cube2[1][1] >= cube1[1][0]:
        return cube1,  [[cube2[0][0],cube2[0][1]],[cube2[1][0],cube1[1][0]-1],[cube2[2][0],cube2[2][1]]], [[cube2[0][0],cube2[0][1]],[cube1[1][0],cube2[1][1]]  ,[cube2[2][0],cube2[2][1]]]
    #z-axis
    elif cube2[2][0] <= cube1[2][1] and cube2[2][1] >= cube1[2][1]:
        return cube1,  [[cube2[0][0],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube1[2][1]]], [[cube2[0][0],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube1[2][1]+1,cube2[2][1]]  ]
    elif cube2[2][0] <= cube1[2][0] and cube2[2][1] >= cube1[2][0]:
        return cube1,  [[cube2[0][0],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube2[2][0],cube1[2][0]-1]], [[cube2[0][0],cube2[0][1]],[cube2[1][0],cube2[1][1]],[cube1[2][0],cube2[2][1]]  ]


insts = []
with open('input.txt', 'r') as fin:
    fin = [
            "on x=10..12,y=10..12,z=10..12",
            "on x=11..13,y=11..13,z=11..13",
            "off x=9..11,y=9..11,z=9..11",
            "on x=10..10,y=10..10,z=10..10",
            ]
    '''
    fin = [
            "on x=-20..26,y=-36..17,z=-47..7",
            "on x=-20..33,y=-21..23,z=-26..28",
            "on x=-22..28,y=-29..23,z=-38..16",
            "on x=-46..7,y=-6..46,z=-50..-1",
            "on x=-49..1,y=-3..46,z=-24..28",
            "on x=2..47,y=-22..22,z=-23..27",
            "on x=-27..23,y=-28..26,z=-21..29",
            "on x=-39..5,y=-6..47,z=-3..44",
            "on x=-30..21,y=-8..43,z=-13..34",
            "on x=-22..26,y=-27..20,z=-29..19",
            "off x=-48..-32,y=26..41,z=-47..-37",
            "on x=-12..35,y=6..50,z=-50..-2",
            "off x=-48..-32,y=-32..-16,z=-15..-5",
            "on x=-18..26,y=-33..15,z=-7..46",
            "off x=-40..-22,y=-38..-28,z=23..41",
            "on x=-16..35,y=-41..10,z=-47..6",
            "off x=-32..-23,y=11..30,z=-14..3",
            "on x=-49..-5,y=-3..45,z=-29..18",
            "off x=18..30,y=-20..-8,z=-3..13",
            "on x=-41..9,y=-7..43,z=-33..15",
            "on x=-54112..-39298,y=-85059..-49293,z=-27449..7877",
            "on x=967..23432,y=45373..81175,z=27513..53682",
    ]
    '''
    part=2
    for line in fin:
        parts =line.split()
        control = parts[0]
        coord = [x[2:] for x in parts[1].split(',')]
        cuboid = []
        for span in coord:
            minmax = [int(x) for x in span.split('..')]
            minmax[-1] = minmax[-1]
            if part == 1:
                if minmax[0] >50 and minmax[1] > 50 or minmax[0]<-50 and minmax[1]<-50:
                    break
            cuboid.append(minmax)
            
        else:
            insts.append([control, cuboid])
i=0
redo = True 
old_len = 0
cubes = [insts.pop(0)]
for inst in insts:
    for i,cube in enumerate(cubes):
        to_add = []
        to_pop = []
        to_check = [inst]
        ic(to_check)
        while len(to_check):
            i+=1
            ic(cube)
            check_me = to_check.pop()
            if total_intersects(check_me[1], cube[1]):
                to_pop.append(i)
                continue
            if intersects(cube[1], check_me[1]):
                ic(check_me)
                _,c2,c3 = split(cube[1],check_me[1])
                to_check.append([check_me[0],c2])
                to_check.append([check_me[0],c3])
            else:
                to_add.append(check_me)
            ic(to_check)
    cubes.extend(to_add)
    for i in to_pop:
        cubes.pop(i)
ic(cubes)

count = 0
for cube in cubes:
    if cube[0] == 'on':
        count+=(cube[1][0][1]-cube[1][0][0])*(cube[1][1][1]-cube[1][1][0])*(cube[1][2][1]-cube[1][2][0])
    if cube[0] == 'off':
        pass
ic(count)
'''   
c1,c2,c3 = split(cubes[0],insts[1][1])
cubes.append([insts[1][0],c2])
cubes.append([insts[1][0],c3])
    for i, inst in enumerate(insts):
        if intersects(inst[1], insts[j][1]) and not total_intersects(inst[1],insts[j][1]): 
            c1,c2,c3 = split(inst[1],insts[j][1])
            cubes.append([inst[0],c2])
            cubes.append([inst[0],c3])
            redo =True
    insts = deepcopy(cubes)
'''
