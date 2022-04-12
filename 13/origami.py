from icecream import ic


class Paper:
    def __init__(self):
        self.data = [[]]

    def add_row(self):
        self.data.append([False for i in range(len(self.data[0]))])

    def add_column(self):
        for row in self.data:
            row.append(False)

    def add_coordinate(self, x, y):
        while len(self.data) <= y:
            self.add_row()
        while len(self.data[y]) <= x:
            self.add_column()
        self.data[y][x] = True

    def __repr__(self):
        return "\n".join(["".join(["#" if x else "." for x in row]) for row in self.data])

    def mirror_axis(self, point, mirror):
        diff = point-mirror
        return point-(diff*2)

    def fold(self, xory, num):
        if xory == 'y':
            #horizontal
            for y, row in enumerate(self.data):
                if y < num: continue
                dest_row_i = self.mirror_axis(y, num)
                new_row = [row[i]+self.data[dest_row_i][i] for i in range(len(self.data[dest_row_i]))]
                self.data[dest_row_i] = new_row
            self.data = self.data[:num]
        else:
            #vertical
            for y, row in enumerate(self.data):
                for x, point in enumerate(row):
                    if x < num: continue
                    dest_col_i = self.mirror_axis(x, num)
                    self.data[y][dest_col_i] = point+row[dest_col_i]
                self.data[y] = row[:num]
            

    def count(self):
        count =0
        for row in self.data:
            for i in row:
                if i: count+=1
        return count

my_paper = Paper()

with open('input.txt', 'r') as fin:
    '''
    fin = [
            "6,10",
            "0,14",
            "9,10",
            "0,3",
            "10,4",
            "4,11",
            "6,0",
            "6,12",
            "4,1",
            "0,13",
            "10,12",
            "3,4",
            "3,0",
            "8,4",
            "1,10",
            "2,14",
            "8,10",
            "9,0",
            "",
            "fold along y=7",
            "fold along x=5"
    ]
    '''
    phase = 0
    for line in fin:
        if line.strip() == "":
            phase += 1
        elif phase == 0:
            parts = line.strip().split(',')
            my_paper.add_coordinate(int(parts[0]), int(parts[1]))
        elif phase ==1:
            parts = line.strip().split()[-1].split('=')
            my_paper.fold(parts[0], int(parts[1]))

    ic(my_paper)
    print(my_paper.count()) 
