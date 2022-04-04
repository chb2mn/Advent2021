part = 2

with open("input.txt", 'r') as fin:
    if part==1:
        x = -1
        total = 0
        for line in fin:
            line = int(line)
            if x > 0 and line > x:
                total+=1
            x = line
        print(total)
    elif part==2:
        meter = []
        total = 0
        for line in fin:
            line = int(line)
            if len(meter) == 3:
                if meter.pop(0) < line:
                    total+=1
            meter.append(line)
        print(total)
