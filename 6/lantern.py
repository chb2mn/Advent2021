from pprint import pprint
import math

orig_mem = {}#days_start -> num_progeny
progeny_mem = {}

def calc_progeny(days_remaining):
    if days_remaining<0: return 0
    if days_remaining in progeny_mem: return progeny_mem[days_remaining]
    #the one I will give birth to, the number of full cycles remaining, the number of progeny the on I gave birth to will have
    #key: calc_progeny for each fish you produce not just the first fist you produce
    progeny = 1+max(0, days_remaining//7) 
    for i in range(days_remaining-7, 0, -7):
        progeny += calc_progeny(i-2)
    progeny_mem[days_remaining] = progeny
    return progeny

def calc_descendants(fish, days_remaining):
    descendants = 0
    for f in fish:
        if f not in orig_mem:
            num_progeny = calc_progeny(days_remaining-f-1)
            orig_mem[f]=num_progeny
        descendants += orig_mem[f]
    return descendants + len(fish)

part = 1
fish = []
with open('input.txt', 'r') as fin:
    for line in fin:
        fish = [int(x) for x in line.strip().split(',')]

#fish = [3,4,3,1,2]
print(fish)
days_remaining = 256

print(calc_descendants(fish, days_remaining))
#pprint(orig_mem)
#pprint(progeny_mem)
