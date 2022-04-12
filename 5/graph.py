from pprint import pprint

part =2

class Field():
    def __init__(self):
        self.field = [[]]

    def set_line(self, p1, p2):
        if max(p1[0], p2[0]) >= len(self.field[0]):
            self.increase_width(max(p1[0], p2[0])+1)
        if max(p1[1], p2[1]) >= len(self.field):
            self.increase_height(max(p1[1], p2[1])+1)
        if p1[0]== p2[0]:
            for i in range(min(p1[1], p2[1]),max(p1[1], p2[1])+1):
                self.field[i][p1[0]] += 1
        elif p1[1]== p2[1]:
            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
                self.field[p1[1]][i] += 1
        elif part ==2:
            #check for diagonals
            m = (p1[1]-p2[1]) / (p1[0]-p2[0])
            if m == 1:
                for i in range(0, max(p1[0], p2[0])- min(p1[0], p2[0])+1):
                    print(min(p1[0], p2[0])+i)
                    print(min(p1[1], p2[1])+i)
                    self.field[min(p1[1], p2[1])+i][min(p1[0],p2[0])+i] +=1
            if m == -1:
                for i in range(0, max(p1[0], p2[0])- min(p1[0], p2[0])+1):
                    self.field[min(p1[1], p2[1])+i][max(p1[0],p2[0])-i] +=1


    def increase_width(self, new_width):
        for row in self.field:
            row.extend([0]*(new_width - len(row)))

    def increase_height(self, new_height):
        for i in range(new_height-len(self.field)):
            self.field.append([0]*len(self.field[0]))

'''
#Test
field = Field()
pprint(field.field)
field.set_line((1,0), (0,1))
pprint(field.field)
field.set_line((1,0), (0,2))
pprint(field.field)
field.set_line((4,5), (2,5))
pprint(field.field)
field.set_line((4,3), (4,5))
pprint(field.field)
field.set_line((2,3), (4,5))
pprint(field.field)
'''

field = Field()
with open('input.txt', 'r') as fin:
    for line in fin:
        line_parts = line.split(' -> ')
        p1_parts = line_parts[0].split(',')
        p2_parts = line_parts[1].split(',')
        p1 = (int(p1_parts[0]), int(p1_parts[1]))
        p2 = (int(p2_parts[0]), int(p2_parts[1]))
        print(p1, p2, len(field.field[0]), len(field.field))
        field.set_line(p1, p2)

crosses = 0
for row in field.field:
    for point in row:
        if point >1:
            crosses+=1
print(crosses)


