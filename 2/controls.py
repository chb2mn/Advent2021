part = 2

if part == 1:
    depth = 0
    x=0
    with open('input.txt', 'r') as fin:
        for line in fin:
            parts = line.split()
            instr = parts[0]
            mag = int(parts[1])
            if instr == 'forward':
                x += mag
            elif instr == 'up':
                depth -= mag
            elif instr == 'down':
                depth += mag
    print(x)
    print(depth)
    print(x*depth)


if part == 2:
    depth = 0
    x=0
    aim = 0
    with open('input.txt', 'r') as fin:
        for line in fin:
            parts = line.split()
            instr = parts[0]
            mag = int(parts[1])
            if instr == 'forward':
                x += mag
                depth += mag*aim
            elif instr == 'up':
                aim -= mag
            elif instr == 'down':
                aim += mag
    print(x)
    print(depth)
    print(x*depth)
