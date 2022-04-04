from icecream import ic

#New Constraint: split cube - freed cube; this means that 
def split(a, b):
    l = [*a, *b]
    l.sort()
    if l[1] == l[2]:
        l[2]+=1 #or l[1]-=1
    return [l[0], l[1]], [l[2], l[3]]

ic(split([1,3],[2,4]))
ic(split([2,4],[1,3]))
ic(split([1,3],[3,4]))
ic(split([1,2],[3,4]))
ic(split([1,5],[2,4]))

