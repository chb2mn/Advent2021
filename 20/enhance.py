from icecream import ic
from copy import deepcopy

preimage = []
alg = ""
with open('input.txt', 'r') as fin:
    alg = fin.readline().strip()
    for line in fin:
        if line.strip() == "":
            continue
        preimage.append(line.strip())

#alg = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
alg = [1 if x == "#" else 0 for x in alg]
#preimage = [
#        "#..#.",
#        "#....",
#        "##..#",
#        "..#..",
#        "..###",
#        ]
image = []
for line in preimage:
    image.append( [1 if x=="#" else 0 for x in line])

def pad_image(image, inf):
    ic(inf)
    image.insert(0,[inf for i in range(len(image[0]))])
    image.insert(0,[inf for i in range(len(image[0]))])
    image.append([inf for i in range(len(image[0]))])
    image.append([inf for i in range(len(image[0]))])
    for row in image:
        row.insert(0,inf)
        row.insert(0,inf)
        row.append(inf)
        row.append(inf)

def get_subimage(x,y,image, inf):
    sub_image = []
    for j in range(y-1,y+2):
        sub_image.append([])
        for i in range(x-1,x+2):
            if j >= len(image) or j < 0 or i >= len(image[0]) or i<0:
                sub_image[j-(y-1)].append(inf)
            else:
                if image[j][i] == "#":
                    ic(x,y,j,i)
                    quit()
                sub_image[j-(y-1)].append(image[j][i])
    return sub_image

def blank_canvas(image):
    new_image = []
    for j in range(len(image)):
        new_image.append([])
        for i in range(len(image[0])):
            new_image[j].append(None)
    return new_image

def subimage2int(subimage):
    binary = ""
    for row in subimage:
        binary += "".join([str(x) for x in row])
    try:
        return int(binary,2)
    except:
        ic(subimage)
        quit()

def enhance(alg, _image, n):
    new_image = blank_canvas(_image)
    for j in range(len(_image)):
        for i in range(len(_image[j])):
            subimage= get_subimage(i,j,_image, n%2)
            alg_i = subimage2int(subimage)
            new_image[j][i] = alg[alg_i]
    return new_image
ic(sum(image[0]))
for i in range(50):
    pad_image(image, i%2)
    pad_image(image, i%2)
    image = enhance(alg, image, i)
    ic(sum(image[0]))
    ic(i)

count = sum([sum(x) for x in image])
ic(count)
