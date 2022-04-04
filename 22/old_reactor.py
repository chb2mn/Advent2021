from icecream import ic

def test_matrix(cubes):
    matrix=[]
    for i in range(26):
        matrix.append([])
        for j in range(26):
            matrix[i].append([])
            for k in range(26):
                matrix[i][j].append(0)
    count = 0
    for cube in cubes:
        ic(cube)
        for x in range(cube[0][0], cube[0][1]+1):
            for y in range(cube[1][0], cube[1][1]+1):
                for z in range(cube[2][0], cube[2][1]+1):
                    if matrix[x][y][z]==1:
                        print("overlap", x,y,z)
                    matrix[x][y][z]=1
                    count += 1
    #ic(matrix)

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
                
    for i in range(3):
        c2axis.append(cube1[i][0] >= cube2[i][0] and cube1[i][1]<=cube2[i][1])
    return all(c1axis) or all(c2axis)

#ic(total_intersects([[1,3],[1,3],[1,3]],[[2,2],[2,2],[2,2]]))
#ic(total_intersects([[2,2],[2,2],[2,2]],[[1,3],[1,3],[1,3]]))
#ic(total_intersects([[2,2],[1,3],[2,2]],[[1,3],[2,2],[1,3]]))
#quit()

def union(cube1, cube2, negate = False):
    if not intersects(cube1, cube2):
        return [cube1,cube2]
    new_cubes = []
    #There will be max 7 cuboids; Front, Back; Top, Bottom; Left, Right, Center
    #Sometimes, the cube won't exit because the cubes aren't total subsets
    #First, let's deal with top and bot. For simplicity, these are the nearest and furthest cubeoids on the y-axis
    #"Top" nearest Y
    if cube1[1][0] < cube2[1][0]:
        new_cube =[[cube1[0][0],cube1[0][1]], [cube1[1][0],cube2[1][0]-1], [cube1[2][0],cube1[2][1]]]
    elif cube1[1][0] > cube2[1][0] and not negate:
        new_cube =[[cube2[0][0],cube2[0][1]], [cube2[1][0],cube1[1][0]-1], [cube2[2][0],cube2[2][1]]]
    else:
        new_cube = [[],[cube1[1][0], cube1[1][0], []]]
    new_cubes.append(new_cube)
    #"Bot" furthest Y
    if cube1[1][1] > cube2[1][1]:
        new_cube =[[cube1[0][0],cube1[0][1]], [cube2[1][1]+1,cube1[1][1]], [cube1[2][0],cube1[2][1]]]
    elif cube1[1][1] < cube2[1][1] and not negate:
        new_cube =[[cube2[0][0],cube2[0][1]], [cube1[1][1]+1,cube2[1][1]], [cube2[2][0],cube2[2][1]]]
    else:
        new_cube = [[],[cube1[1][1], cube1[1][1], []]]
    new_cubes.append(new_cube)
    miny = new_cubes[0][1][1]+1
    maxy = new_cubes[1][1][0]-1
    #Next, let's deal with front and back. For simplicity, these are the nearest and furthest cubeoids on the y-axis
    #"Front" nearest Z
    if cube1[2][0] < cube2[2][0]:
        new_cube = [[cube1[0][0], cube1[0][1]],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[cube1[2][0], cube2[2][0]-1]]
    elif cube1[2][0] > cube2[2][0] and not negate:
        new_cube = [[cube2[0][0], cube2[0][1]],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[cube2[2][0], cube1[2][0]-1]]
    else:
        new_cube = [[],[],[cube1[2][0], cube1[2][0]]]
    new_cubes.append(new_cube)
    #"Back" furthest Z
    if cube1[2][1] > cube2[2][1]:
        new_cube = [[cube1[0][0], cube1[0][1]],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[cube2[2][1]+1, cube1[2][1]]]
    elif cube1[2][1] < cube2[2][1] and not negate:
        new_cube = [[cube2[0][0], cube2[0][1]],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[cube1[2][1]+1, cube2[2][1]]]
    else:
        new_cube = [[],[],[cube1[2][1], cube1[2][1]]]
    new_cubes.append(new_cube)
    #
    #Almost done, let's deal with left and right. For simplicity, ese are the nearestnd furthest cubeoids on the x-axis
    #"left" nearest X
    if cube1[0][0] < cube2[0][0]:
        new_cube = [[cube1[0][0], cube2[0][0]-1],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[new_cubes[2][2][1]+1, new_cubes[3][2][0]-1]]
    elif cube1[0][0] > cube2[0][0] and not negate:
        new_cube = [[cube2[0][0], cube1[0][0]-1],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[new_cubes[2][2][1]+1, new_cubes[3][2][0]-1]]
    else:
        new_cube = [[cube1[0][0], cube1[0][0]],[],[]]
    new_cubes.append(new_cube)
    #"right" furthest X
    if cube1[0][1] > cube2[0][1]:
        new_cube = [[cube2[0][1]+1, cube1[0][1]],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[new_cubes[2][2][1]+1, new_cubes[3][2][0]-1]]
    elif cube1[0][1] < cube2[0][1] and not negate:   
        new_cube = [[cube1[0][1]+1, cube2[0][1]],[new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],[new_cubes[2][2][1]+1, new_cubes[3][2][0]-1]]
    else:
        new_cube = [[cube1[0][1], cube1[0][1]],[],[]]
    new_cubes.append(new_cube)
    
    if not negate:
        final_cube = [
                [new_cubes[4][0][1]+1,new_cubes[5][0][0]-1],
                [new_cubes[0][1][1]+1,new_cubes[1][1][0]-1],
                [new_cubes[2][2][1]+1,new_cubes[3][2][0]-1]
                ]
        new_cubes.append(final_cube)
    new_cubes = [x for x in new_cubes if all([len(y) for y in x])]
    return new_cubes

#ic(union([[0,5],[0,5],[0,5]], [[1,6],[1,6],[1,6]]))
#ic(union([[1,6],[1,6],[1,6]], [[0,5],[0,5],[0,5]]))
#ic(union([[1,6],[1,5],[1,6]], [[0,5],[0,5],[0,5]]))
#ic(union([[1,6],[2,3],[1,6]], [[0,5],[0,5],[0,5]]))
#ic(union([[1,1],[1,1],[1,1]], [[0,2],[0,2],[0,2]]))
#
#ic(union([[0,5],[0,5],[0,5]], [[1,6],[1,6],[1,6]],negate=True))
#ic(union([[1,6],[1,6],[1,6]], [[0,5],[0,5],[0,5]],negate=True))
#ic(union([[1,6],[1,5],[1,6]], [[0,5],[0,5],[0,5]],negate=True))
#ic(union([[1,6],[2,3],[1,6]], [[0,5],[0,5],[0,5]],negate=True))
#ic(union([[1,1],[1,1],[1,1]], [[0,2],[0,2],[0,2]],negate=True))

#test_matrix(union([[0,5],[0,5],[0,5]], [[1,6],[1,6],[1,6]]))
#quit()

class oldReactor:
    def __init__(self, boundary):
        self.ignited_cubes = {}
        self.boundary = boundary
    def ignite_cube(self, x,y,z):
        if max(x,y,z) <= self.boundary and min(x,y,z) >= -self.boundary:
            self.ignited_cubes[(x,y,z)] = 1
    def quench_cube(self, x,y,z):
        del(self.ignited_cubes[(x,y,z)])
    def ignite(self, xs,ys,zs):
        for i in range(*xs):
            for j in range(*ys):
                for k in range(*zs):
                    self.ignite_cube(i,j,k)
    def quench(self, xs,ys,zs):
        for i in range(*xs):
            for j in range(*ys):
                for k in range(*zs):
                    try:
                        self.quench_cube(i,j,k)
                    except KeyError:
                        pass
    def get_num(self):
        return len(self.ignited_cubes)

#my_reactor = Reactor(50)


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

cubes = []

for i, inst in enumerate(insts):
    if inst[0] == "on":
        if not len(cubes):
            cubes.append(inst[1])
            continue
        to_pop = []
        to_add = []
        for i, cube in enumerate(cubes):
            if intersects(cube, inst[1]):
                if not total_intersects(cube, inst[1]):
                    ic(cube, inst[1])
                    new_cubes = union(cube, inst[1])
                    to_pop.append(i)
                    to_add.extend(new_cubes)
            else:
                to_add.append(cube)
        cubes.extend(to_add)
        for pop in to_pop:
            cubes.pop(pop)
    if inst[0] == 'off':
        to_pop = []
        to_add = []
        for i, cube in enumerate(cubes):
            if intersects(cube, inst[1]):
                ic(cube, inst[1])
                new_cubes = union(cube, inst[1], negate=True)
                to_pop.append(i)
                to_add.extend(new_cubes)
        cubes.extend(to_add)
        for pop in to_pop:
            ic(pop)
            cubes.pop(pop)
        test_matrix(cubes)
        quit()
    ic(cubes)

count=0
for cube in cubes:
    for x in range(cube[0][0],cube[0][1]+1):
        for y in range(cube[1][0],cube[1][1]+1):
            for z in range(cube[2][0],cube[2][1]+1):
                count+=1
ic(count)

               
