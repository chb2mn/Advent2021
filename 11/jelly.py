from icecream import ic


data = []
with open('input.txt','r') as fin:
    #fin = [
    #        "5483143223",
    #        "2745854711",
    #        "5264556173",
    #        "6141336146",
    #        "6357385478",
    #        "4167524645",
    #        "2176841721",
    #        "6882881134",
    #        "4846848554",
    #        "5283751526",
    #]
    for line in fin:
        data.append([])
        for i in line.strip():
            data[-1].append(int(i))

ic(data)
total = 0
def step_data(data):
    global total
    exploders=[]
    for y, line in enumerate(data):
        for x, jelly in enumerate(line):
            data[y][x] += 1
            if data[y][x] == 10:
                exploders.append((y,x))
    while len(exploders) > 0:
        explode(data,exploders)
    for y, line in enumerate(data):
        for x, jelly in enumerate(line):
            if data[y][x] ==10:
                total += 1
                data[y][x] = 0

def incr_jelly(data, exploders, y, x):
    if data[y][x]<10:
        data[y][x] += 1
        if data[y][x] == 10:
            exploders.append((y,x))

def explode(data, exploders):
    y, x = exploders.pop()
    if x > 0:
        incr_jelly(data, exploders, y, x-1)
        if y > 0:
            incr_jelly(data, exploders, y-1, x-1)
        if y < len(data)-1:
            incr_jelly(data, exploders, y+1, x-1)
    if x < len(data[y])-1:
        incr_jelly(data, exploders, y, x+1)
        if y > 0:
            incr_jelly(data, exploders, y-1, x+1)
        if y < len(data)-1:
            incr_jelly(data, exploders, y+1, x+1)
    if y > 0:
        incr_jelly(data, exploders, y-1, x)
    if y < len(data)-1:
        incr_jelly(data, exploders, y+1, x)

steps =100000000
for i in range(steps):
    step_data(data)
    print(i+1)
    ic(data)
    if not any([any(line) for line in data]):
        break
ic(total)
