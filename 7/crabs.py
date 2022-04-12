
my_input = []
with open('input.txt', 'r') as fin:
    for line in fin:
        my_input =[int(x) for x in line.split(',')]

#my_input = [16,1,2,0,4,2,7,1,2,14]


import statistics
part =2
if part ==1:
    median = statistics.median(my_input)
    print(median)

    fuel = 0
    for crab in my_input:
        fuel += abs(crab-median)

    print(fuel)

if part ==2:
    mean = round(statistics.mean(my_input))
    print(mean)
    
    def calc_fuel(my_input, mean):
        fuel = 0
        for crab in my_input:
            fuel += (1+abs(crab-mean))*abs(crab-mean)/2
        return fuel


    print(calc_fuel(my_input, mean-2))
    print(calc_fuel(my_input, mean-1))
    print(calc_fuel(my_input, mean))
